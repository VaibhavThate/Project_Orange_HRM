from faker import Faker
import uuid

faker = Faker()

def generate_emp():
    return {
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "employee_id": str(uuid.uuid4().int)[:8]
    }

