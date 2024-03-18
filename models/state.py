#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import models
from models.city import City

Base = declarative_base()

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship(
                "City", cascade="all, delete, delete-orphan",
                backref="state"
                )
    @property
    def cities(self):
        """Getter attribute for cities"""
        from models import storage
        cities_list = []
        for city in list(storage.all("City").values()):
            if city.state_id == self.id:
                cities_list.append(city)
        return cities_list
