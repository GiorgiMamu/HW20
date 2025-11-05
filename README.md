# — დავალება —

შექმენით Flask აპლიკაცია, რომელშიც მომხმარებლებს შეეძლებათ <br>
შექმნან თავიანთთვის Note-ები, ანუ პირადი ჩანაწერები, რომლებსაც <br>
მხოლოდ თვითონ დაინახავენ და სხვა მომხმარებელი ამას ვერ გააკეთებს.<br>

#### სტრუქტურა:
SecureNotes/ <br>
│  app.py<br>
│  models.py<br>
│  forms.py<br>
│ db.py<br>
│<br>
│── templates/<br>
│  base.html<br>
│  register.html<br>
│  login.html<br>
│  notes.html<br>
│ add_note.html<br>
│<br>
│── instance/<br>
│notes.db<br>
│<br>
│── static/<br>
│style.css<br>
│<br>
│.gitignore<br>
│README.md<br>
│requirements.txt<br>

აუცილებლად უნდა დაარეგისტრიროთ მომხმარებელი და ასევე უნდა<br>
ჰქონდეს შესაძლებლობა გაიაროს ავტორიზაცია, მხოლოდ ამის შემდეგ<br>
უნდა შეეძლოს note-ის შექმნა. (ასევე უნდა ჰქონდეს logout-ის საშუალება)<br>

#### საჭირო გამოსაყენებელი ტექნოლოგიები: <br>
1. UserMixin
2. password hash 
3. generate_password_hash
4. check_password_hash 
5. RegisterForm
6. LoginForm
7. NoteForm
8. @login_required