import httpx
import zipfile
import pandas as pd
from pathlib import Path

CMS_ICD10_URL = "https://www.cms.gov/medicare/coding-billing/icd-10-codes"
HCPCS_URL    = "https://www.cms.gov/medicare/coding-billing/healthcare-common-procedure-system"
HCPCS_UPDATE_URL = "https://www.cms.gov/medicare/coding-billing/healthcare-common-procedure-system/quarterly-update"

class CMSCodeFeedIngestor:
    """Downloads, extracts, and normalizes CMS code files."""

    def __init__(self, s3_client, bucket: str):
        self.s3 = s3_client
        self.bucket = bucket

    async def fetch_icd10_cm(self, fiscal_year: str) -> pd.DataFrame:
        url = f"https://www.cms.gov/files/zip/FY{fiscal_year}-April-Update-Code-Descriptions-in-Tabular-Order.zip"
        async with httpx.AsyncClient() as client:
            r = await client.get(url, follow_redirects=True)
        # Extract, parse fixed-width or delimited code file
        return self._parse_icd10_flat(r.content)

    def _parse_icd10_flat(self, content: bytes) -> pd.DataFrame:
        # CMS distributes as fixed-width; normalize to code, description, category
        ...

    def upload_to_s3(self, df: pd.DataFrame, key: str):
        parquet_buf = df.to_parquet()
        self.s3.put_object(Bucket=self.bucket, Key=key, Body=parquet_buf)