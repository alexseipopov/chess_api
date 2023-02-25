class SerializeTable:
    def __init__(self, model, **filter):
        self.model = model
        self.filter = filter

    def get_columns(self):
        return self.model.__table__.columns.keys()

    def all_data(self):
        result = []
        for line in self.model.query.all():
            result.append({col.name: getattr(line, col.name) for col in self.model.__table__.columns})
        return result

    def data(self):
        result = []
        for line in self.model.query.filter_by(**self.filter):
            result.append({col.name: getattr(line, col.name) for col in self.model.__table__.columns})
        return result


def validate_request(model, data) -> bool:
    columns = model.__table__.columns.keys()
    return all([True if param in columns else False for param in data])


def get_invalid_params(model, data) -> list:
    columns = model.__table__.columns.keys()
    return [param for param in data if param not in columns]
