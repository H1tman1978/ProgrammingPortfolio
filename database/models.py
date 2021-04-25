from . import db


class Address(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True
                   )
    street_address = db.Column(db.String(100),
                               nullable=False
                               )
    street_address2 = db.Column(db.String(100),
                                nullable=True
                                )
    city = db.Column(db.String(30),
                     nullable=False
                     )
    state = db.Column(db.String(2),
                      nullable=False
                      )
    zip_code = db.Column(db.String(10),
                         nullable=False
                         )

    def __init__(self, street, street2, city, state, zip_code):
        self.street_address = street
        self.street_address2 = street2
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def __repr__(self):
        return "<Address {}> {}, {}, {}, {}  {}".format(self.id,
                                                        self.street_address,
                                                        self.street_address2,
                                                        self.city,
                                                        self.state,
                                                        self.zip_code
                                                        )
