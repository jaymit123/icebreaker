import requests
import os


def scrape_linkedin_profile(linkedin_profile_url: str):
    """
    scrape information from linkedin profiles.
    Manually scrape the information from the linkedin profile.
    """
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    headers = {"Authorization": "Bearer " + os.environ.get("PROXYCURL_API_KEY")}
    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=headers
    )

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
