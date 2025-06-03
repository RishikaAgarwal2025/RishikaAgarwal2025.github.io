# Load libraries
import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import string
import random

# Create a Faker instance to generate random data
fake = Faker()
Faker.seed(42)

# Create sets to ensure uniqueness
user_ids = set()
usernames = set()
emails = set()
phone_numbers = set()

def generate_unique_id():
    """Generate a unique user ID consisting of 5 random letters and digits."""
    max_attempts = 10000
    attempts = 0

    while attempts < max_attempts:
        user_id = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        if user_id not in user_ids:
            user_ids.add(user_id)
            return user_id
        attempts += 1

    raise RuntimeError("Exceeded max attempts to generate a unique user ID.")

def generate_unique_username():
    """Generate a unique username."""
    max_attempts = 10000
    attempts = 0

    while attempts < max_attempts:
        username = fake.user_name()
        if username not in usernames:
            usernames.add(username)
            return username
        attempts += 1

    raise RuntimeError("Exceeded max attempts to generate a unique username.")

def generate_unique_email(username):
    """Generate a unique email."""
    max_attempts = 10000
    attempts = 0

    while attempts < max_attempts:
        email = f"{username}@{fake.free_email_domain()}"
        if email not in emails:
            emails.add(email)
            return email
        attempts += 1

    raise RuntimeError("Exceeded max attempts to generate a unique email.")

def generate_unique_phone():
    """Generate a unique UK phone number."""
    max_attempts = 10000
    attempts = 0

    while attempts < max_attempts:
        second_digit = random.choice(range(1, 10))  
        remaining_digits = ''.join(random.choices(string.digits, k=9))
        phone_number = f"44{second_digit}{remaining_digits}"

        if phone_number not in phone_numbers:
            phone_numbers.add(phone_number)
            return phone_number

        attempts += 1

    raise RuntimeError("Exceeded max attempts to generate a unique phone number.")
def generate_age():
    """Generate an age value using a normal distribution with a mean of 25 
    and a standard deviation of 10. Ensures the age falls within 18 to 70."""
    while True:
        age = int(random.gauss(25, 10))
        if 18 <= age <= 70:
            return age
        
def select_plan(gender, age):
    """Select a subscription plan based on gender and age"""
    if gender == "female":
        # Adjust probabilities so that females are more likely to choose the Premium plan
        plan_weights = [12, 22, 66]  # Basic (18%), Standard (28%), Premium (54%)
    else:
        # Males are more likely to choose the Standard plan over Premium
        plan_weights = [31, 48, 21]  # Basic (31%), Standard (48%), Premium (21%)

    # Increase the probability of selecting Premium for younger users
    if age < 25:
        plan_weights = [12, 25, 63]  # Basic (12%), Standard (25%), Premium (63%)
    elif age < 35:
        plan_weights = [37, 38, 25]  # Basic (57%), Standard (18%), Premium (25%)
    
    return random.choices([1, 2, 3], weights=plan_weights, k=1)[0]  # 1=Basic, 2=Standard, 3=Premium
    
def get_subscription_duration(gender, plan_id):
    """Assign a subscription duration range based on gender and plan type with heavily weighted probabilities"""
    if gender == "female":
        # 여성은 거의 무조건 긴 구독 기간을 선택하도록 설정
        plan_durations = {
            1: [18, 21, 24],  
            2: [36, 42, 48],  
            3: [60, 66, 72]  
        }
        weights = {
            1: [1, 3, 6],  # 24개월이 거의 필수적으로 선택됨
            2: [1, 2, 7],  # 48개월이 가장 자주 선택됨
            3: [1, 2, 10]  # 72개월이 거의 확정적으로 선택됨
        }
    elif gender == "male":
        # 남성은 거의 무조건 짧은 구독 기간을 선택하도록 설정
        plan_durations = {
            1: [1, 3, 6],  
            2: [6, 12, 18, 24],  
            3: [12, 18, 24]  
        }
        weights = {
            1: [6, 3, 1],  # 1개월이 거의 필수적으로 선택됨
            2: [5, 3, 2, 1],  # 6~12개월이 자주 선택됨
            3: [5, 3, 2]  # 12개월이 가장 많이 선택됨
        }
    elif gender in ["non-binary", "prefer not to say"]:
        # Non-binary & prefer not to say는 중간 정도의 구독 기간을 선택하도록 설정
        plan_durations = {
            1: [6, 9, 12, 15],  
            2: [18, 24, 30, 36],  
            3: [36, 42, 48]  
        }
        weights = {
            1: [2, 3, 4, 5],  # 중간 정도의 확률 분포
            2: [2, 3, 4, 5],  # 중간 정도의 확률 분포
            3: [1, 2, 5]  # 48개월이 조금 더 자주 선택됨
        }
    else:
        raise ValueError("Invalid gender specified")

    return random.choices(plan_durations[plan_id], weights=weights[plan_id])[0]

# Generate user data
users = []
user_id_list = []  # Store user IDs to ensure subscription user IDs match

for _ in range(535):  # Generate data for 535 users
    user_id = generate_unique_id() # Generate a unique user ID
    user_id_list.append(user_id) # Store the user ID for later reference

    username = generate_unique_username() # Generate a unique username
    
    users.append({
        "user_id": user_id, # Unique user identifier
        "username": username, # Unique username
        "password": fake.password(), # Randomly generated password
        "email": generate_unique_email(username), # Generate unique email based on username
        "phone_number": generate_unique_phone(), # Generate a unique UK phone number
        "age": generate_age(), # Generate a valid age
        "gender": random.choices(
            ["female", "male", "non-binary", "prefer not to say"],
            weights=[48, 31, 15, 6],  # Probability distribution
            k=1
        )[0]  # Select one gender based on weights
    })

# Data Generation Settings
num_subscriptions = 535  # Number of subscriptions
num_issues = 520  # Number of weekly published issues
num_sessions = 1500  # Number of reading sessions

start_date_range = datetime(2017, 1, 1)  # Earliest possible subscription start date
end_date_range = datetime(2025, 3, 20)  # Latest possible subscription end date

# Lists to store generated data for subscriptions, payments, issues, reading sessions, and issue-topic mappings
subscriptions = []
payments = []
issues = []
reading_sessions = []
issue_topics = []

# Sets to track unique IDs
subscription_ids = set()
payment_ids = set()
issue_ids = set()
session_ids = set()

# Generate a unique subscription ID (5 characters: at least 1 letter & 1 digit)
def generate_subscription_id():
    """Generate a unique subscription ID (5 random uppercase letters and digits, ensuring mix)."""
    while True:
        sub_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if any(c.isalpha() for c in sub_id) and any(c.isdigit() for c in sub_id):  # Ensure at least 1 letter & 1 digit
            if sub_id not in subscription_ids:
                subscription_ids.add(sub_id)
                return sub_id

# Generate a unique payment ID (7 characters: at least 1 letter & 1 digit)
def generate_payment_id():
    """Generate a unique payment ID (7 random lowercase letters, ensuring mix)."""
    while True:
        pay_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))
        if any(c.isalpha() for c in pay_id) and any(c.isdigit() for c in pay_id):  # Ensure at least 1 letter & 1 digit
            if pay_id not in payment_ids:
                payment_ids.add(pay_id)
                return pay_id
            
# Generate a unique issue ID (4 characters: at least 1 letter & 1 digit)
def generate_issue_id():
    """Generate a unique issue ID (4 characters, at least one letter and one digit)."""
    while True:
        # Ensure at least one letter and one digit
        letters = random.choices(string.ascii_uppercase, k=1)  # At least one letter
        digits = random.choices(string.digits, k=1)  # At least one digit
        remaining = random.choices(string.ascii_uppercase + string.digits, k=2)  # Remaining characters
        
        issue_id = ''.join(random.sample(letters + digits + remaining, 4))  # Shuffle to randomize position
        
        if issue_id not in issue_ids:  # Ensure uniqueness
            issue_ids.add(issue_id)
            return issue_id

# Generate a unique session ID (6 characters: at least 1 letter & 1 digit)
def generate_session_id():
    """Generate a unique session ID (6 random lowercase letters and digits, ensuring mix)."""
    while True:
        sess_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        if any(c.isalpha() for c in sess_id) and any(c.isdigit() for c in sess_id):  # Ensure at least 1 letter & 1 digit
            if sess_id not in session_ids:
                session_ids.add(sess_id)
                return sess_id

# Define payment method probabilities
payment_methods = [1, 2, 3, 4, 5, 6, 7]  # Payment method IDs
payment_weights = [41, 8, 3, 10, 30, 5, 3]  # Probability weights (higher means more frequent)

# Ensure num_subscriptions does not exceed available users
num_subscriptions = min(num_subscriptions, len(user_id_list))

# Select unique user IDs
selected_user_ids = random.sample(user_id_list, num_subscriptions)

for i in range(num_subscriptions):
    subscription_id = generate_subscription_id()
    user_id = selected_user_ids[i]

    # Retrieve user information
    user_info = next(user for user in users if user["user_id"] == user_id)
    gender = user_info["gender"]
    age = user_info["age"]

    # Step 1: Select subscription plan based on gender & age
    plan_id = select_plan(gender, age)

    while True:
     # Step 2: Randomly select a start date between 2017 and 2024 (excluding 2025)
     random_year = random.randint(2017, 2024)
     random_month = random.randint(1, 12)
     random_day = random.randint(1, 28)  # Restrict to 28 days max (to account for February)
     start_date = datetime(random_year, random_month, random_day)

     # Step 3: Assign subscription duration based on gender and plan type
     duration_months = get_subscription_duration(gender, plan_id)

     # Step 4: Set the maximum allowed subscription end date
     max_end_date = datetime(2025, 3, 20)

     # Adjust duration to increase the probability of ending in April or December
     roll = random.random()

     if roll < 0.5:  # 50% 확률로 4월 종료 (1등)
        preferred_end_months = [4]
        for extra_months in range(12):  # 최대 12개월 추가해서 4월로 맞춤
            potential_end_date = start_date + relativedelta(months=duration_months + extra_months)
            if potential_end_date.month in preferred_end_months:
                duration_months += extra_months
                break  

     elif roll < 0.75:  # 25% 확률로 12월 종료 (2등)
        preferred_end_months = [12]
        for extra_months in range(12):
            potential_end_date = start_date + relativedelta(months=duration_months + extra_months)
            if potential_end_date.month in preferred_end_months:
                duration_months += extra_months
                break  

     elif roll < 0.90:  # 15% 확률로 2, 6, 9, 11월 종료 (살짝 높은 확률)
        preferred_end_months = [2, 6, 9, 11]
        for extra_months in range(6):
            potential_end_date = start_date + relativedelta(months=duration_months + extra_months)
            if potential_end_date.month in preferred_end_months:
                duration_months += extra_months
                break  

    # 나머지 10% 확률은 기본적인 구독 종료 유지

    # Step 5: Calculate the end date (exactly N months after the start date)
    end_date = start_date + relativedelta(months=duration_months)
    if end_date > max_end_date:
        end_date = max_end_date  # Explicitly cap the end date

    # Step 6: Introduce a probability for subscriptions to remain active (i.e., no end date)
    null_end_probabilities = {1: 0.27, 2: 0.48, 3: 0.73}  
    if random.random() < null_end_probabilities[plan_id]:  
        end_date = None  # Some users will maintain their subscriptions indefinitely

    # Step 7: Ensure the start date is never later than the end date
    if end_date is None or start_date < end_date:
        break  # Exit the loop if conditions are met

# Step 8: Store subscription data
subscriptions.append({
    "subscription_id": subscription_id,
    "user_id": user_id,
    "plan_id": plan_id,
    "start_date": start_date.date(),
    "end_date": end_date.date() if end_date else None,
})

# Generate payment records for each subscription
for subscription in subscriptions:
    subscription_id = subscription["subscription_id"]
    user_id = subscription["user_id"]
    start_date = datetime.combine(subscription["start_date"], datetime.min.time())
    end_date = (
        datetime.combine(subscription["end_date"], datetime.min.time())
        if subscription["end_date"]
        else None
    )
    
    # Retrieve user age
    user_info = next(user for user in users if user["user_id"] == user_id)
    age = user_info["age"]

    # Set different payment method probabilities based on age
    if age < 35:  # Young customers prefer Apple Pay (5) & Google Pay (6)
        payment_methods = [1, 2, 3, 4, 5, 6, 7]  
        payment_weights = [10, 6, 3, 7, 42, 28, 4]  
    else:  # Older customers prefer Credit Card (1)
        payment_methods = [1, 2, 3, 4, 5, 6, 7]  
        payment_weights = [37, 13, 4, 20, 15, 6, 5]  
        
    # Initialise payment_date to the subscription start date
    payment_date = start_date

    while True:
        # If the subscription has an end date, check if payment_date exceeds it
        if end_date and payment_date >= end_date:
            break  # Stop generating payments if the payment_date exceeds the end_date

        # If the subscription is active (end_date is None), limit payments to a reasonable date (e.g., 2025-03-20)
        if not end_date and payment_date >= datetime(2025, 3, 20):
            break  # Stop generating payments if the payment_date exceeds the maximum allowed date

        # Add the payment record
        payments.append({
            "payment_id": generate_payment_id(),
            "user_id": user_id,
            "subscription_id": subscription_id,
            "payment_method_id": random.choices(payment_methods, weights=payment_weights, k=1)[0],
            "payment_date": payment_date.date()
        })

        # Move to the next month
        payment_date += relativedelta(months=1)

# Generate a set of unique release dates
available_dates = set()
while len(available_dates) < num_issues:
    available_dates.add(fake.date_between(start_date=start_date_range, end_date=end_date_range))

# Convert the set to a sorted list to maintain chronological order
available_dates = sorted(available_dates)

# Store issues
for issue_number, release_date in enumerate(available_dates, start=1):
    issue_id = generate_issue_id()  # Generate a unique issue ID

    issues.append({
        "issue_id": issue_id,  # Unique identifier for the issue
        "issue_number": issue_number,  # Sequential issue number (1, 2, ..., num_issues)
        "release_date": release_date,  # The official release date of the issue (Now Unique)
    })

for issue in issues:  
    issue_id = issue["issue_id"]
    assigned_topics = set()  # Use a set to prevent duplicate topic assignments

    num_topics = random.randint(1, 3)  # Randomly assign 1 to 3 topics per issue
    while len(assigned_topics) < num_topics:
        topic_id = random.randint(1, 15)  # Select a random topic ID from the range 1 to 15
        assigned_topics.add(topic_id)  # Ensure unique topics by using a set

    # Store the assigned topics for each issue in the issue_topics list
    for topic_id in assigned_topics:
        issue_topics.append({
            "issue_id": issue_id,
            "topic_id": topic_id
        })
        
# Define preferred topics for different user groups with extreme differences
young_female_fav_topics = [1, 3, 5, 7, 14]  
young_male_fav_topics = [1, 6, 12, 14, 15] 
young_nonbinary_fav_topics = [1, 6, 7, 14, 15]  

mid_female_fav_topics = [1, 4, 7, 8, 11]  
mid_male_fav_topics = [1, 4, 9, 11, 12] 
mid_nonbinary_fav_topics = [1, 4, 7, 11, 15] 

old_female_fav_topics = [1, 4, 7, 10, 11]  
old_male_fav_topics = [1, 2, 9, 10, 12] 
old_nonbinary_fav_topics = [1, 3, 9, 10, 15]  

# Assign user preferences based on gender and age
user_fav_topics = {}
for user in users:
    user_id = user["user_id"]
    age = user["age"]
    gender = user["gender"]

    if 18 <= age <= 24:  # 젊은 층 (18~24세)
        if gender == "female":
            user_fav_topics[user_id] = young_female_fav_topics
        elif gender == "male":
            user_fav_topics[user_id] = young_male_fav_topics
        else:  # non-binary / prefer not to say
            user_fav_topics[user_id] = young_nonbinary_fav_topics

    elif 25 <= age <= 34:  # 중간 연령층 (25~34세)
        if gender == "female":
            user_fav_topics[user_id] = mid_female_fav_topics
        elif gender == "male":
            user_fav_topics[user_id] = mid_male_fav_topics
        else:  # non-binary / prefer not to say
            user_fav_topics[user_id] = mid_nonbinary_fav_topics

    else:  # 35세 이상 (구독 중년층)
        if gender == "female":
            user_fav_topics[user_id] = old_female_fav_topics
        elif gender == "male":
            user_fav_topics[user_id] = old_male_fav_topics
        else:  # non-binary / prefer not to say
            user_fav_topics[user_id] = old_nonbinary_fav_topics

# Map each user to their subscription plan for easy reference
user_plan_map = {sub["user_id"]: sub["plan_id"] for sub in subscriptions}

# Create a dictionary to store the set of issues read by each user to prevent duplicates
user_issue_map = {user["user_id"]: set() for user in users}

for user_subscription in subscriptions:
    user_id = user_subscription["user_id"]
    
    # Convert subscription start and end dates to datetime format for comparison
    subscription_start = datetime.combine(user_subscription["start_date"], datetime.min.time())
    subscription_end = (
        datetime.combine(user_subscription["end_date"], datetime.min.time())
        if user_subscription["end_date"] # If the subscription has an end date, use it
        else datetime(2025, 3, 20) # Otherwise, assume an active subscription until March 20, 2025
    )

    # Retrieve the subscription plan and the user's preferred topics
    plan_id = user_plan_map[user_id]
    fav_topics = user_fav_topics[user_id]

    # Create a weighted list of issues based on the presence of preferred topics
    weighted_issues = []
    for issue in issues:
        issue_id = issue["issue_id"]
        release_date = issue["release_date"]
        
        # Skip issues that were released outside the user's subscription period
        if not (subscription_start.date() <= release_date <= subscription_end.date()):
            continue  

        # Retrieve the list of topics associated with the issue
        issue_topic_ids = [row["topic_id"] for row in issue_topics if row["issue_id"] == issue_id]

        # Calculate a weight based on how many of the user's preferred topics are in the issue
        weight = sum(1 for topic in issue_topic_ids if topic in fav_topics)
        # If the issue contains preferred topics, increase its probability of being read by adding it multiple times
        if weight > 0:
            weighted_issues.extend([issue] * (weight * 5))  # More preferred topics → Higher chance of being selected
    
    # If no preferred issues are found, fall back to the general issue list
    valid_issues = weighted_issues if weighted_issues else issues

    # Keep track of the issues a user has already read to prevent duplication
    already_read_issues = user_issue_map[user_id]

    # Determine the number of issues the user will read based on their subscription plan
    if plan_id == 3:  # Premium Plan
        num_readings = random.randint(3, 7) # Premium users read between 3 to 7 issues.
    elif plan_id == 2:  # Standard Plan
        num_readings = random.randint(2, 5)  # Standard users read between 2 to 5 issues.
    else:  # Basic Plan
        num_readings = random.randint(1, 2) # Basic users read between 1 to 3 issues.

    # Ensure no duplicate issues are assigned to the user
    for _ in range(num_readings):
        # Filter issues that the user has not yet read
        available_issues = [issue for issue in valid_issues if issue["issue_id"] not in already_read_issues]
        if not available_issues:
            break  # If no remaining issues are available, stop assigning

        # Randomly select an issue from the available options
        issue = random.choice(available_issues)
        issue_id = issue["issue_id"]
        already_read_issues.add(issue_id)  # Add the issue to the user's set of read issues to prevent duplicates

        # Ensure the reading session start date falls within the user’s subscription period
        latest_start_date = max(issue["release_date"], subscription_start.date())  
        earliest_end_date = subscription_end.date()  
        
        # If the selected start date is after the subscription end date, skip this issue
        if latest_start_date > earliest_end_date:  
            continue 
        
        # Generate a random start date within the valid reading period
        start_date = fake.date_between(start_date=latest_start_date, end_date=earliest_end_date)
        
        # Determine the percentage of the issue read based on the user's plan, gender & age
        age_group = None
        if 18 <= age <= 24:
            age_group = "young"  # 가장 높은 read rate
        elif 25 <= age <= 34:
             age_group = "mid"  # 중간 정도 read rate
        else:
             age_group = "old"  # 낮은 read rate

        # Determine the percentage of the issue read based on the user's plan & gender
        if plan_id == 3:  # Premium users
           if gender == "female":
              base_prob = 0.85 if age_group == "young" else (0.70 if age_group == "mid" else 0.50)
              percentage_read = 100.00 if random.random() < base_prob else round(random.uniform(70.00, 99.99), 2)
           elif gender == "male":
              base_prob = 0.40 if age_group == "young" else (0.30 if age_group == "mid" else 0.15)
              percentage_read = 100.00 if random.random() < base_prob else round(random.uniform(30.00, 95.00), 2)
           else:  # Non-binary / Prefer not to say
               base_prob = 0.60 if age_group == "young" else (0.50 if age_group == "mid" else 0.30)
               percentage_read = 100.00 if random.random() < base_prob else round(random.uniform(50.00, 98.00), 2)

        elif plan_id == 2:  # Standard users
          if gender == "female":
             base_prob = 0.65 if age_group == "young" else (0.50 if age_group == "mid" else 0.35)
             percentage_read = 100.00 if random.random() < base_prob else round(random.uniform(50.00, 99.99), 2)
          elif gender == "male":
             base_prob = 0.25 if age_group == "young" else (0.20 if age_group == "mid" else 0.10)
             percentage_read = 100.00 if random.random() < base_prob else round(random.uniform(20.00, 90.00), 2)
          else:  # Non-binary / Prefer not to say
              base_prob = 0.45 if age_group == "young" else (0.35 if age_group == "mid" else 0.25)
              percentage_read = 100.00 if random.random() < base_prob else round(random.uniform(40.00, 95.00), 2)

        else:  # Basic users
          if gender == "female":
             base_prob = 0.40 if age_group == "young" else (0.30 if age_group == "mid" else 0.20)
             percentage_read = 100.00 if random.random() < base_prob else round(random.uniform(30.00, 95.99), 2)
          elif gender == "male":
            base_prob = 0.15 if age_group == "young" else (0.10 if age_group == "mid" else 0.05)
            percentage_read = 100.00 if random.random() < base_prob else round(random.uniform(10.00, 85.00), 2)
          else:  # Non-binary / Prefer not to say
            base_prob = 0.30 if age_group == "young" else (0.20 if age_group == "mid" else 0.15)
            percentage_read = 100.00 if random.random() < base_prob else round(random.uniform(25.00, 92.00), 2)

        reading_sessions.append({
            "session_id": generate_session_id(),
            "user_id": user_id,
            "issue_id": issue_id,  # Issue ID without duplication.
            "start_date": start_date,
            "end_date": end_date if end_date else None,
            "percentage_read": percentage_read
        })

# Convert lists into DataFrames and save them as CSV files
users_df = pd.DataFrame(users)
subscriptions_df = pd.DataFrame(subscriptions)
payments_df = pd.DataFrame(payments)
issues_df = pd.DataFrame(issues)
issue_topics_df = pd.DataFrame(issue_topics)
reading_sessions_df = pd.DataFrame(reading_sessions)

# Save each DataFrame as a CSV file
users_df.to_csv("users.csv", index=False)
subscriptions_df.to_csv("subscriptions.csv", index=False)
payments_df.to_csv("payments.csv", index=False)
issues_df.to_csv("issues.csv", index=False)
issue_topics_df.to_csv("issue_topics.csv", index=False)
reading_sessions_df.to_csv("user_reading_sessions.csv", index=False)

print("Data generation completed!")