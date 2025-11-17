"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal

# Example schemas (keep for reference):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Crypto Recovery specific schema

class RecoveryRequest(BaseModel):
    """
    Recovery requests for lost/compromised crypto assets
    Collection name: "recoveryrequest"
    """
    vorname_nachname: str = Field(..., description="Vollständiger Name")
    email: EmailStr = Field(..., description="E-Mail-Adresse")
    kontaktweg: Literal["E-Mail", "Telefon", "Telegram", "Signal", "WhatsApp"] = Field(
        "E-Mail", description="Bevorzugter Kontaktweg"
    )
    telefon_oder_handle: Optional[str] = Field(None, description="Telefonnummer oder Handle je nach Kontaktweg")
    wallet_typ: Literal["Hardware", "Software", "Custodial", "Seed Phrase", "Sonstiges"] = Field(
        ..., description="Art des Wallets"
    )
    netzwerk: Optional[str] = Field(None, description="Blockchain/Netzwerk (z. B. Bitcoin, Ethereum, Solana)")
    betroffene_assets: Optional[str] = Field(None, description="Betroffene Coins/Tokens")
    vorfall_typ: Literal[
        "Verlorener Zugriff",
        "Phishing/Hack",
        "Fehlerhafte Transaktion",
        "Beschädigte Hardware",
        "Unbekannt"
    ] = Field(..., description="Art des Vorfalls")
    transaktionshash: Optional[str] = Field(None, description="Optionaler Transaktionshash/ID")
    betrag_oder_wert: Optional[str] = Field(None, description="Geschätzter Betrag/Wert")
    beschreibung: str = Field(..., description="Kurze Beschreibung des Vorfalls")
    dringlichkeit: Literal["Niedrig", "Mittel", "Hoch", "Kritisch"] = Field("Mittel", description="Dringlichkeit")
    datenschutz_einwilligung: bool = Field(..., description="Einwilligung in Datenverarbeitung gemäß Datenschutzerklärung")
