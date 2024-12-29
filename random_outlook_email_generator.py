import random
import string

def generate_random_email():
    # 定义可能的名字和姓氏
    first_names = [
        "Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Henry", "Ivy", "Jack",
        "Kate", "Leo", "Mia", "Noah", "Olivia", "Paul", "Quinn", "Ryan", "Sophia", "Thomas",
        "Uma", "Vincent", "Willow", "Xander", "Yara", "Zoe", "Adam", "Bella", "Carter", "Diana",
        "Ethan", "Fiona", "Gabriel", "Hannah", "Isaac", "Julia", "Kevin", "Lily", "Mason", "Natalie",
        "Oscar", "Penelope", "Quentin", "Rachel", "Samuel", "Tina", "Ursula", "Victor", "Wendy", "Xavier",
        "Yvonne", "Zachary", "Avery", "Benjamin", "Chloe", "Daniel", "Emma", "Freya", "George", "Harper",
        "Isabella", "Jackie", "Katherine", "Liam", "Maya", "Nathan", "Ophelia", "Parker", "Quincy", "Ruby",
        "Sebastian", "Taylor", "Uma", "Violet", "William", "Xenia", "Yasmine", "Zack", "Aria", "Bryan",
        "Cecilia", "Dylan", "Ella", "Finn", "Grace", "Hunter", "Iris", "Jade", "Kai", "Luna",
        "Milo", "Nina", "Owen", "Piper", "Quinn", "Riley", "Sienna", "Theo", "Uma", "Violet",
        "Wyatt", "Xander", "Yara", "Zoe"
    ]
    last_names = [
        "Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor",
        "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson",
        "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King",
        "Wright", "Lopez", "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter",
        "Mitchell", "Perez", "Roberts", "Turner", "Phillips", "Campbell", "Parker", "Evans", "Edwards", "Collins",
        "Stewart", "Sanchez", "Morris", "Rogers", "Reed", "Cook", "Morgan", "Bell", "Murphy", "Bailey",
        "Rivera", "Cooper", "Richardson", "Cox", "Howard", "Ward", "Torres", "Peterson", "Gray", "Ramirez",
        "James", "Watson", "Brooks", "Kelly", "Sanders", "Price", "Bennett", "Wood", "Barnes", "Ross",
        "Henderson", "Coleman", "Jenkins", "Perry", "Powell", "Long", "Patterson", "Hughes", "Flores", "Washington",
        "Butler", "Simmons", "Foster", "Gonzales", "Bryant", "Alexander", "Russell", "Griffin", "Diaz", "Hayes"
    ]

    while True:
        # 随机选择一个名字和姓氏
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)

        # 生成随机的字符串作为邮箱名称的一部分
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))

        # 生成完整的邮箱地址
        email = f"{first_name.lower()}_{random_string}.{last_name.lower()}@outlook.com"

        yield email

# 创建一个生成器对象
email_generator = generate_random_email()

# 生成并打印多个随机的Outlook邮箱名称
for _ in range(1):
    print(next(email_generator))