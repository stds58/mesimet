
import os
import sys
import time
import pandas as pd
import sqlalchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import MetaData
from sqlalchemy import Column, Integer, String, NVARCHAR, Boolean, Float, Index
from sqlalchemy.dialects.mssql import SQL_VARIANT
from sqlalchemy.schema import CreateSchema
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc


class OsnModel(DeclarativeBase):
    metadata=MetaData(schema = 'zalivka')


class Template(OsnModel):
    __tablename__ =  'template'
    id_template = Column(Integer, primary_key=True, index=True, autoincrement=False, nullable=False)
    description = Column(NVARCHAR, nullable=False)
    cnt_fld = Column(Integer, nullable=False)
    dop1 = Column(NVARCHAR)


class TemplateInfo(OsnModel):
    __tablename__ =  'template_info'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    id_template = Column(Integer, nullable=False)
    id_fld = Column(Integer, nullable=False)
    field = Column(NVARCHAR, nullable=False)


class ListFiles(OsnModel):
    __tablename__ =  'list_files'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    id_template = Column(Integer, nullable=True)
    path = Column(NVARCHAR(255), nullable=False)
    filename = Column(NVARCHAR(255), nullable=False)  #, unique=True
    listname = Column(NVARCHAR(31), nullable=False)
    on = Column(Boolean, nullable=True)
    cnt_fld = Column(Integer, nullable=True)
    status = Column(NVARCHAR(255), nullable=True)
    dop1 = Column(NVARCHAR(255), nullable=True)
    dop2 = Column(NVARCHAR(255), nullable=True)
    dop3 = Column(NVARCHAR(255), nullable=True)
    time_sek = Column(Float, nullable=True)


class Work:
    def __init__(self):
        self.engine = self.get_engine


    def timer(f):
        def wrapper(*args, **kwargs):
            t = time.time()
            f(*args, **kwargs)
            dt = time.time() - t
            return dt
        return wrapper


    def get_engine(self, hostname, dbname, user, pwd):
        self.engine = create_engine(
            f"mssql+pyodbc://{user}:{pwd}@{hostname}/{dbname}"
            "?driver=ODBC+Driver+17+for+SQL+Server",
            fast_executemany=True, echo=False)
        return self.engine


    def create_table(self):
        conn = self.engine.connect()
        if 'zalivka' not in conn.dialect.get_schema_names(conn):
            conn.execute(CreateSchema('zalivka'))
            conn.commit()
        OsnModel.metadata.create_all(bind=self.engine)
        conn.close()

    def select_template(self):
        engine = self.engine
        conn = engine.connect()
        self.dic_tmp = {}
        Session = sessionmaker(autoflush=False, bind=engine)
        with Session(autoflush=False, bind=engine) as db:
            test2 = db.query(Template).all()
            for p in test2:
                self.dic_tmp[p.id_template] = p.description
        conn.close()
        return self.dic_tmp


    def select_list_files(self):
        engine = self.engine
        conn = engine.connect()
        L = []
        Session = sessionmaker(autoflush=False, bind=engine)
        with Session(autoflush=False, bind=engine) as db:
            db = db.query(ListFiles).all()
            for p in db:
                L.append(p.id)
            self.id = max(L)
        conn.close()
        return self.id


    def insert_template(self, id_template, description, cnt_fld):
        engine = self.engine
        Session = sessionmaker(autoflush=False, bind=engine)
        with Session(autoflush=False, bind=engine) as db:
            try:
                data1 = Template(id_template=id_template, description=description, cnt_fld=cnt_fld)
                db.add_all([data1])  # добавляем в бд
                db.commit()  # сохраняем изменения
                db.refresh(data1)  # обновляем состояние объекта
            except exc.ProgrammingError as e:
                pass
            except exc.IntegrityError as e:
                pass


    def insert_template_info(self, id_template, id_fld, field):
        engine = self.engine
        Session = sessionmaker(autoflush=False, bind=engine)
        with Session(autoflush=False, bind=engine) as db:
            try:
                test2 = db.query(TemplateInfo).all()
                status = 0
                for p in test2:
                    if not status and p.id_template == id_template and p.id_fld == id_fld and p.field == field:
                        status = 1 #есть шаблон
                if not status:
                    data1 = TemplateInfo(id_template=id_template, id_fld=id_fld, field=field)
                    db.add_all([data1])  # добавляем в бд
                    db.commit()  # сохраняем изменения
                    db.refresh(data1)  # обновляем состояние объекта
            except exc.ProgrammingError as e:
                pass
            except exc.IntegrityError as e:
                pass
            except AttributeError as e:
                data1 = TemplateInfo(id_template=id_template, id_fld=id_fld, field=field)
                db.add_all([data1])  # добавляем в бд
                db.commit()  # сохраняем изменения
                db.refresh(data1)  # обновляем состояние объекта


    def insert_list_files(self, id_template, path, filename, listname, cnt_fld):
        engine = self.engine
        Session = sessionmaker(autoflush=False, bind=engine)
        with Session(autoflush=False, bind=engine) as db:
            try:
                data1 = ListFiles(id_template=id_template, path=path, filename=filename, listname=listname, cnt_fld=cnt_fld)
                db.add_all([data1])  # добавляем в бд
                db.commit()  # сохраняем изменения
                db.refresh(data1)  # обновляем состояние объекта
            except exc.ProgrammingError as e:
                pass
            except exc.IntegrityError as e:
                pass


    def update_list_files(self,  dt):
        engine = self.engine
        dic = self.select_template()  # получить список шаблонов
        id = self.select_list_files()
        Session = sessionmaker(autoflush=False, bind=engine)
        with Session(autoflush=False, bind=engine) as db:
            row = db.query(ListFiles).filter(ListFiles.id == id).first()
            row.time_sek = dt
            db.commit()


    def sqlcol(self, param):
        dtypedict = {}
        for i, j in zip(param.columns, param.dtypes):
            #dtypedict.update({i: SQL_VARIANT})
            dtypedict.update({i: NVARCHAR()})
        return dtypedict


    @timer
    def download(self, path, filename, sheet):
        dic_tmp = {}  # {номер шаблона: шапка}
        df = pd.read_excel(path + filename, sheet_name=sheet, header=0)
        heads = df.columns.values.tolist()  # получить заголовки
        description = '[' + '],['.join(map(str, heads)) + ']'
        dic_tmp = self.select_template()  # получить список шаблонов
        status = 0
        number_tmpl = None
        for key, value in dic_tmp.items():
            if value == description:
                status = 1
                number_tmpl = key
        if not status:  # если список полей из текущего листа не совпадает с шаблоном, добавляем его
            if not dic_tmp.keys():
                id_template = 1
            else:
                id_template = max(dic_tmp.keys()) + 1
        else:
            id_template = number_tmpl
        cnt_fld = len(heads)
        self.insert_template(id_template, description, cnt_fld)
        for field, id_fld in zip(heads, range(1, len(heads) + 1)):
            self.insert_template_info(id_template, id_fld, field)
        self.insert_list_files(id_template, path, filename, sheet, cnt_fld)
        # залить данные
        engine = self.engine
        slovar = self.sqlcol(df)
        tablename = self.select_list_files()
        df.to_sql(str(tablename), engine, schema='zalito', if_exists='append', index=True, index_label='id',dtype=slovar)


    def get_sheetlist(self, path):
        self.create_table()
        filelist = os.listdir(path)
        for filename in filelist: #итерировать файлы
            #wb = load_workbook(path+filename, read_only=True)
            wb = pd.read_excel(path+filename, sheet_name=None)
            #print('wb.keys()',wb.keys())
            for i in wb.keys(): #итерировать листы
                sheet = str(i)
                #print(f'{filename}:',sheet)
                dt = self.download(path, filename, sheet)
                self.update_list_files(dt)
                #print(dt)



a = Work()
a.get_engine('***', '***', '***', '***')
a.get_sheetlist("E:/import/xxx/")

