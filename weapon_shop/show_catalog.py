# =====================================================
#  weapon_shop/show_catalog.py — คนรับผิดชอบ: ROBLOX SHADOW STEALER MAFIA 007 Lnwza
#  หน้าที่: แสดงรายการอาวุธทั้งหมดที่มีขาย
# =====================================================
from data import weapons_catalog

def show_catalog():
#   - print อาวุธทุกชิ้นใน weapons_catalog บรรทัดละชิ้น (รหัส, ชื่อ, ราคา, พลังโบนัส)
    for weapon_id, weapon in weapons_catalog.items():
        print(f"weapon ID : {weapon_id} | {weapon['name']} | price: {weapon['price']} | bonus: {weapon['bonus']}")


# ทดสอบเฉพาะไฟล์ตัวเอง: พิมพ์  python -m weapon_shop.show_catalog
if __name__ == "__main__":
    show_catalog()   # ต้องเห็นอาวุธครบ 3 ชิ้น