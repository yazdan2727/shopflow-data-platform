from sqlalchemy.orm import Session

from app.products.models import Product


class ProductRepository:

    def create(
        self,
        db: Session,
        product: Product,
    ) -> Product:
        db.add(product)
        db.commit()
        db.refresh(product)

        return product

    def get_by_id(
        self,
        db: Session,
        product_id: str,
    ) -> Product | None:
        return (
            db.query(Product)
            .filter(Product.id == product_id)
            .first()
        )

    def list(
        self,
        db: Session,
    ) -> list[Product]:
        return (
            db.query(Product)
            .order_by(Product.created_at.desc())
            .all()
        )