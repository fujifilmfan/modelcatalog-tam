from pydantic import BaseModel, HttpUrl, EmailStr
from typing import Optional
from enum import Enum


class ContactTypeEnum(str, Enum):
    maintainer = "maintainer"
    author = "author"
    point_of_contact = "point_of_contact"


class Person(BaseModel):
    """Person or contact model

    Fields
    ------
    name : str
        Contact name to display
        Alison P Appling
    orcid : HttpUrl
        Full URL for ORCID profile, see: https://orcid.org/
        https://orcid.org/0000-0003-3638-8572
    email : EmailStr
        Valid email address
        aappling@usgs.gov
    author_type : str
        Specification for type of contact
        author
    thumbnail_avatar_url : HttpUrl
        Direct link to personal profile image
        https://prd-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/styles/content_grid/public/thumbnails/image/appling_headshot.png
    organization : str
        USGS organization
        USGS Water Resources Mission Area
    job_title : str
        Short job title
        Data Scientist
    sciencebase_id : str
        Sciencebase Directory link to profile (see https://www.sciencebase.gov/directory/person/68008)
        68008
    usgs_staffprofile_url : HttpUrl
        Direct link to USGS Staff Profile webpage
        https://www.usgs.gov/staff-profiles/alison-appling
    usgs_gitlab_id: int
        Internal gitlab user identifier
    github_profile: str
        Public GitHub user profile
        aappling-usgs
    usgs_employee: bool
        USGS employee True = yes; False = no
        1
    """

    _version: str = "v1.0.0"

    name: str
    author_type: ContactTypeEnum = "author"
    usgs_employee: Optional[bool] = False
    orcid: Optional[HttpUrl]
    email: Optional[EmailStr]
    thumbnail_avatar_url: Optional[HttpUrl]
    organization: Optional[str]
    job_title: Optional[str]
    sciencebase_id: Optional[str]
    usgs_staffprofile_url: Optional[HttpUrl]
    usgs_gitlab_id: Optional[str]
    github_profile: Optional[str]
