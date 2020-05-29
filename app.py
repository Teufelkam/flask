from flask import Flask, request, jsonify

from studentService import Student_Service

app = Flask(__name__)

student_service = Student_Service()


@app.route('/')
def get_students():
    print(student_service.get_students())
    return jsonify(data=[student.serialize for student in student_service.get_students()])


@app.route('/<string:name>')
def get_student_by_name(name):
    student = student_service.get_student_by_name(name)

    if student is None:
        return jsonify(error="Student with name: " + name + " does not exist")
    else:
        return jsonify(student.serialize)


@app.route('/', methods=['POST'])
def insert_student():
    name = request.get_json().get("name")
    surname = request.get_json().get("surname")
    return jsonify(data=student_service.insert_student(name, surname).serialize)


@app.route('/', methods=['PUT'])
def update_student():
    name = request.get_json().get("name")
    surname = request.get_json().get("surname")
    id = request.get_json().get("id")
    if student_service.get_student_by_id(id) is None:
        return jsonify(error="Student with id: " + id + "does not exist")
    return jsonify(data=student_service.udpate_student(id, name, surname).serialize)


@app.route('/<int:id>', methods=['DELETE'])
def delete_student(id):
    if student_service.delete_student_by_id(id):
        return jsonify("Student deleted")
    else:
        return jsonify("Student does not exist")


if __name__ == '__main__':
    app.run()
