from ResourceSchema import Resources
from ReferenceSchema import References
from PersonSchema import Person
from IdentifierSchema import Identifier
from RelatedCatalogItemSchema import RelatedCatalogItem

from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from enum import Enum


class ModelTypeEnum(str, Enum):
    model = "model"
    framework = "framework"
    tool = "tool"
    testbed = "testbed"


class TypeKeywordEnum(str, Enum):
    theoretical = "Theoretical"
    empirical = "Empirical"
    physics_based = "Physics-based"
    process_based = "Process-based"
    statistical = "Statistical"
    geospatial = "Geospatial"


class BasicProfile(BaseModel):
    """Basic metadata profile

    Fields
    ------
    item_type : ModelTypeEnum
        model, tool, framework, testbed
    name : str
        title
    description : str
        abstract or general description
    organization: bool = True
        True = usgs ; False = external
    external_organization_name: Optional[str]
    release_date : str
        Date
    last_update : str
        Date
    author : Optional[List[Person]]
        The author(s) or developer(s) of this content.
    contact : Optional[List[Person]]
        Person(s) responsible for maintenance of the model or item.
    version : str
        Latest release version v1.0.0
    how_to_cite: Optional[str]
        Preferred citation format
    usgs_missionarea: Optional[str]
        USGS mission area
    identifier: Optional[List[Identifier]]
        Identifiers related to the model
    programming_language: Optional[str]
        Primary programming language used for the modeling
    license: Optional[str]
       CC0 see: https://creativecommons.org/publicdomain/zero/1.0/legalcode
    resources: Optional[Resources]
        Custom object containing advanced resource section
    references: Optional[References]
        Custom object containing advanced reference section
    science_keywords: Optional[str]
        Topical science keywords that will help for discovering the item. Preferred to use terms from the USGS Thesaurus please see: https://apps.usgs.gov/thesaurus/
    type_keywords: Optional[TypeKeywordEnum]
    other_keywords: Optional[str]
        For example, platform and mode (Jupyter, Graphical User Interface, etc).
    image: Optional[HttpUrl]
        Header image for the model profile page
    related_catalog_item: Optional[RelatedCatalogItem]

    Example
    -------
    >>> BasicProfile(item_type="model",
    ...              name="COAWST",
    ...              description="sample description")
    BasicProfile(item_type=<ModelTypeEnum.model: 'model'>, name='COAWST', description='sample description', organization=True, external_organization_name=None, release_date=None, last_update=None, subtitle=None, author=None, contact=None, version=None, how_to_cite=None, usgs_missionarea=None, identifier=None, programming_language=None, license='CC0', resources=None, references=None, science_keywords=None, type_keywords=None, other_keywords=None, image=None, related_catalog_item=None)
    """

    _version: str = "v1.0.0"

    item_type: ModelTypeEnum = "model"
    name: str
    description: str
    organization: bool = True
    external_organization_name: Optional[str]
    release_date: Optional[str]
    last_update: Optional[str]
    subtitle: Optional[str]
    author: Optional[List[Person]]
    contact: Optional[List[Person]]
    version: Optional[str]
    how_to_cite: Optional[str]
    usgs_missionarea: Optional[str]
    identifier: Optional[List[Identifier]]
    programming_language: Optional[str]
    license: Optional[str] = "CC0"
    resources: Optional[Resources]
    references: Optional[References]
    science_keywords: Optional[List[str]]
    type_keywords: Optional[TypeKeywordEnum]
    other_keywords: Optional[str]
    image: Optional[HttpUrl]
    related_catalog_item: Optional[RelatedCatalogItem]
