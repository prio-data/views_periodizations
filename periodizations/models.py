
from sqlalchemy import Column, Date, Integer, ForeignKey, Text, CheckConstraint
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class SplitGroup(Base):
    """
    Groups splits into semantic units, such as "model runs". Splits are ordered
    by split.rank.
    """
    __tablename__ = "splitgroup"
    pk = Column(Integer, primary_key = True)

    description = Column(Text, default = "")

    splits = Column(Integer, ForeignKey("split.pk"))

class Split(Base):
    """
    Groups timespans into "splits", for example train-test splits or
    train-test-holdout splits. Spans are ordered by span.rank
    """
    __tablename__ = "split"
    __table_args__ = (
            CheckConstraint( "rank>0", name = "positiverank"),
            )

    pk = Column(Integer, primary_key = True)
    description = Column(Text, default = "")
    spans = Column(Integer, ForeignKey("span.pk"))
    rank = Column(Integer)

class Span(Base):
    """
    Timespan with metadata.
    """
    __tablename__ = "span"
    __table_args__ = (
            CheckConstraint( "start>\"end\"", name = "checkdates"),
            CheckConstraint( "rank>0", name = "positiverank"),
            )

    pk = Column(Integer, primary_key = True)
    rank = Column(Integer)
    kind = Column(Text)
    start = Column("start", Date)
    end = Column("end", Date)
