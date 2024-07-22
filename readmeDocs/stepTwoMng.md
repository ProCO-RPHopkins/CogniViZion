# Detailed description of Step Two

Step 2: Database Design and Models

1. Define Database Schema
    - Decide on the database system (e.g., SQLite, PostgreSQL, MySQL).
    - Create a new database (if not already done).
    - Define the schema for the following entities:
        - User: Stores user information (username, email, password hash, etc.).
        - StudyMaterials: Represents uploaded study materials (PDFs or text).
        - Concepts: Stores identified key concepts.
        - Progress: Tracks user progress (answered questions, mastery level, etc.).
2. Create SQLAlchemy Models
    - In your Flask app, create a models.py file.
    - Define SQLAlchemy models for each entity:

**User Model - Code**
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    # Add other relevant fields (e.g., profile image, study preferences)

**StudyMaterials Model - Code**
class StudyMaterials(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content_text = db.Column(db.Text, nullable=False)
    # Add other relevant fields (e.g., file name, upload timestamp)

**Concepts Model - Code**
class Concepts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    study_material_id = db.Column(db.Integer, db.ForeignKey('study_materials.id'), nullable=False)
    concept_text = db.Column(db.Text, nullable=False)
    # Add other relevant fields (e.g., concept type, related topics)

**Progress Model - Code**
class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    concept_id = db.Column(db.Integer, db.ForeignKey('concepts.id'), nullable=False)
    mastery_level = db.Column(db.Float, nullable=False)  # e.g., percentage mastered
    # Add other relevant fields (e.g., last accessed timestamp)

**Continue Steps**
3. Database Relationships
    - Define relationships between models (e.g., one-to-many, many-to-one):
        - A user can have multiple study materials.
        - Each study material can have multiple concepts.
        - Progress is associated with both users and concepts.
4. Migrations
    - Use Flask-Migrate to create database migrations.
    - Run flask db init, flask db migrate, and flask db upgrade to apply changes.
5. Seed Initial Data (Optional)
    - If needed, create a script to seed initial data (e.g., sample users, study materials).