from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def testpaper(request):
    quiz ='''
      <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Quiz</title>
    <style>
        body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 0;
    padding: 0;
    color: #333;
    background-color: #e9ecef;
}

header {
    background-color: #007bff;
    color: white;
    padding: 1.5em 0;
    text-align: center;
    border-bottom: 4px solid #0056b3;
}

header h1 {
    margin: 0;
    font-size: 2em;
}

main {
    padding: 20px;
}

.quiz-container {
    background-color: white;
    border-radius: 12px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    padding: 30px;
    max-width: 800px;
    margin: auto;
    border: 1px solid #dee2e6;
}

.question {
    margin-bottom: 25px;
}

.question h2 {
    font-size: 1.4em;
    margin-bottom: 15px;
    color: #495057;
}

.question label {
    display: block;
    margin: 8px 0;
    font-size: 1.1em;
}

.question input[type="radio"] {
    margin-right: 10px;
    cursor: pointer;
}

button {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 12px 20px;
    font-size: 1.1em;
    border-radius: 6px;
    cursor: pointer;
    display: block;
    margin: 30px auto 0;
    transition: background-color 0.3s ease;
}

button:hover {
    background-color: #0056b3;
}

footer {
    background-color: #007bff;
    color: white;
    text-align: center;
    padding: 12px;
    position: fixed;
    width: 100%;
    bottom: 0;
    border-top: 4px solid #0056b3;
}

footer p {
    margin: 0;
    font-size: 0.9em;
}

/* Media Queries for Responsive Design */
@media (max-width: 1024px) {
    .quiz-container {
        padding: 20px;
    }
    
    .question h2 {
        font-size: 1.3em;
    }
    
    button {
        padding: 10px 18px;
        font-size: 1em;
    }
}

@media (max-width: 768px) {
    .quiz-container {
        padding: 15px;
    }
    
    .question h2 {
        font-size: 1.2em;
    }
    
    button {
        padding: 8px 15px;
        font-size: 0.9em;
    }
}

@media (max-width: 480px) {
    .quiz-container {
        padding: 10px;
    }
    
    .question h2 {
        font-size: 1em;
    }
    
    .question label {
        font-size: 0.9em;
    }
    
    button {
        padding: 6px 12px;
        font-size: 0.8em;
    }
}

    </style>
</head>
<body>
    <header>
        <h1>Python Quiz</h1>
    </header>
    <main>
        <section class="quiz-container">
            <form id="quizForm">
                <div class="question">
                    <h2>1. What is the output of <code>print(type([]))</code> in Python?</h2>
                    <label><input type="radio" name="q1" value="a"> `<class 'list'>`</label>
                    <label><input type="radio" name="q1" value="b"> `<class 'dict'>`</label>
                    <label><input type="radio" name="q1" value="c"> `<class 'tuple'>`</label>
                    <label><input type="radio" name="q1" value="d"> `<class 'set'>`</label>
                </div>
                <div class="question">
                    <h2>2. Which of the following is used to define a function in Python?</h2>
                    <label><input type="radio" name="q2" value="a"> `function`</label>
                    <label><input type="radio" name="q2" value="b"> `def`</label>
                    <label><input type="radio" name="q2" value="c"> `func`</label>
                    <label><input type="radio" name="q2" value="d"> `define`</label>
                </div>
                <div class="question">
                    <h2>3. How do you insert comments in Python code?</h2>
                    <label><input type="radio" name="q3" value="a"> `/* comment */`</label>
                    <label><input type="radio" name="q3" value="b"> `<!-- comment -->`</label>
                    <label><input type="radio" name="q3" value="c"> `# comment`</label>
                    <label><input type="radio" name="q3" value="d"> `-- comment --`</label>
                </div>
                <div class="question">
                    <h2>4. What is the purpose of the <code>self</code> keyword in Python?</h2>
                    <label><input type="radio" name="q4" value="a"> To refer to the current instance of the class</label>
                    <label><input type="radio" name="q4" value="b"> To define a class</label>
                    <label><input type="radio" name="q4" value="c"> To create a new class</label>
                    <label><input type="radio" name="q4" value="d"> To access global variables</label>
                </div>
                <div class="question">
                    <h2>5. Which method can be used to remove whitespace from the beginning and end of a string?</h2>
                    <label><input type="radio" name="q5" value="a"> `strip()`</label>
                    <label><input type="radio" name="q5" value="b"> `trim()`</label>
                    <label><input type="radio" name="q5" value="c"> `remove()`</label>
                    <label><input type="radio" name="q5" value="d"> `clear()`</label>
                </div>
                <button type="submit">Submit Quiz</button>
            </form>
        </section>
    </main>
    <footer>
        <p>&copy; 2024 Quiz Inc. All rights reserved.</p>
    </footer>
</body>
</html>




        '''
    return HttpResponse(quiz)

def result(request):
    r ="<h1>This is result page</h1>"
    return HttpResponse(r)