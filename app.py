from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure database connection
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

# Initialize database
db = SQLAlchemy()
db.init_app(app)

with app.app_context():
    db.create_all()

# Define models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    # Add other user-related fields (password hash, email, etc.)

# Create sample users
user1 = User(username="alice")
user2 = User(username="bob")

class StudyMaterials(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content_text = db.Column(db.Text, nullable=False)
    # Add other fields (file path, metadata, etc.)
    # Create sample study materials
study_material1 = StudyMaterials(user_id=1, content_text="Introduction to Python")
study_material2 = StudyMaterials(user_id=2, content_text="Flask Framework")

class Concepts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    study_material_id = db.Column(db.Integer, db.ForeignKey('study_materials.id'), nullable=False)
    concept_text = db.Column(db.Text, nullable=False)
    # Add other relevant fields (e.g., concept type, related topics)

# Create sample concepts
concept1 = Concepts(study_material_id=1, concept_text="Variables")
concept2 = Concepts(study_material_id=1, concept_text="Loops")
concept3 = Concepts(study_material_id=2, concept_text="Routing")
concept4 = Concepts(study_material_id=2, concept_text="Templates")

class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    concept_id = db.Column(db.Integer, db.ForeignKey('concepts.id'), nullable=False)
    mastery_level = db.Column(db.Float, nullable=False)  # e.g., percentage mastered
    # Add other relevant fields (e.g., last accessed timestamp)

# Create sample progress records
progress1 = Progress(user_id=1, concept_id=1, mastery_level=0.8)
progress2 = Progress(user_id=1, concept_id=2, mastery_level=0.6)
progress3 = Progress(user_id=2, concept_id=3, mastery_level=0.9)
progress4 = Progress(user_id=2, concept_id=4, mastery_level=0.7)

# Add the sample data to the session
db.session.add_all([user1, user2, study_material1, study_material2, concept1, concept2, concept3, concept4,
                    progress1, progress2, progress3, progress4])

# Commit the changes to the database
db.session.commit()

# Print a success message
print("Sample data inserted successfully!")

@app.route('/')
def index():
    return "Welcome to Cogni-ViZion! Your ed-tech platform for streamlined test preparation."


if __name__ == '__main__':
    app.run(debug=True)