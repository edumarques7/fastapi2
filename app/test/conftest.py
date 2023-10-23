import pytest
from passlib.context import CryptContext
from app.db.connection import Session
from app.db.models import Category as CategoryModels
from app.db.models import Product as ProductModel
from app.db.models import User as UserModel


crypt_context = CryptContext(schemes=['sha256_crypt'])


@pytest.fixture()
def db_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()


@pytest.fixture()
def categories_on_db(db_session):
    categories = [
        CategoryModels(name='Roupa', slug='roupa'),
        CategoryModels(name='Carro', slug='carro'),
        CategoryModels(name='Itens de cozinha', slug='itens-de-cozinha'),
        CategoryModels(name='Decoracao', slug='decoracao'),
    ]

    for category in categories:
        db_session.add(category)
    db_session.commit()

    for category in categories:
        db_session.refresh(category)

    yield categories

    for category in categories:
        db_session.delete(category)
    db_session.commit()


@pytest.fixture()
def product_on_db(db_session):
    category = CategoryModels(name='Carro', slug='carro')
    db_session.add(category)
    db_session.commit()

    product = ProductModel(
        name='Camisa Abibas',
        slug='camisa-abibas',
        price=100.99,
        stock=20,
        category_id=category.id
    )

    db_session.add(product)
    db_session.commit()

    yield product

    db_session.delete(product)
    db_session.delete(category)
    db_session.commit()


@pytest.fixture()
def products_on_db(db_session):
    category = CategoryModels(name='Roupa', slug='roupa')
    db_session.add(category)
    db_session.commit()
    db_session.refresh(category)

    products = [
        ProductModel(name='Camisa Mike', slug='camisa-mike', price=100, stock=10, category_id=category.id),
        ProductModel(name='Moletom Mike', slug='moletom', price=100, stock=10, category_id=category.id),
        ProductModel(name='Camiseta', slug='camiseta-mike', price=100, stock=10, category_id=category.id),
        ProductModel(name='Calca', slug='calca', price=100, stock=10, category_id=category.id),
    ]

    for product in products:
        db_session.add(product)
    db_session.commit()

    for product in products:
        db_session.refresh(product)

    yield products

    for product in products:
        db_session.delete(product)

    db_session.delete(category)
    db_session.commit()


@pytest.fixture()
def user_on_db(db_session):
    user = UserModel(
        username='Dudu',
        password=crypt_context.hash('pass#')
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    yield user

    db_session.delete(user)
    db_session.commit()


