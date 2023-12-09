from sqlmodel import Session, SQLModel
from sqlmodel.sql.expression import SelectOfScalar


class SQLRepository:
    def __init__(self, entity: SQLModel, db: Session):
        self.entity = entity
        self.db = db

    def create_entity(self, entity: SQLModel):
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def get_entities_with_statement(self, statement: SelectOfScalar):
        return self.db.exec(statement)

    def get_all_entities(self):
        return self.db.query(self.entity)

    def get_entity_by_id(self, entity_id: int):
        return self.db.query(self.entity).filter(self.entity.id == entity_id).first()
