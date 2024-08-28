from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    home = '''
       <h1 align= "center" style="color:Blue">Sistec Gandhinagar</h1>
       <br>
       <p>Welcome to sistec</p>


'''
    return HttpResponse(home)

def about(request):
    about = '''
        <h1 align ="center" style = "color:red">About Sistec</h1>
        <br>
        <p>
Sagar Institute of Science and Technology (SISTec®), established in the year 2007, is one of the best engineering colleges, located in the heart of the state, the city of lakes - Bhopal. SISTec is the brand name for technical colleges under the umbrella of the Sagar Group of Institutions®. Boasting state-of-the-art facilities, a diverse student body, and a talented pool of faculty, SISTec has established itself as a leader in providing quality education offering B.Tech., Management, and M.Tech. programs. The academic programs are designed to meet the needs and interests of students from all backgrounds, making SISTec the perfect place to jumpstart your future. The brand has a strong motivation towards innovation in curriculum implementation. It further aspires to be a part of the education revolution in Technical education, impacting futuristic technologies in the Indian framework. In this process, it aims to be one of the finest providers of technical education in India.</p>

'''
    return HttpResponse(about)

def contact(request):
    cont ='''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
   
    <style> 
        body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    color: #333;
}

header {
    background-color: #4CAF50;
    color: white;
    padding: 1em 0;
    text-align: center;
}

main {
    padding: 20px;
}

.contact-form,
.contact-info,
.map {
    margin-bottom: 20px;
}

.contact-form form {
    display: flex;
    flex-direction: column;
}

.contact-form label {
    margin: 5px 0 2px;
}

.contact-form input,
.contact-form textarea {
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

.contact-form button {
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.contact-form button:hover {
    background-color: #45a049;
}

.contact-info {
    background-color: #f9f9f9;
    padding: 15px;
    border-radius: 5px;
}

.contact-info p {
    margin: 5px 0;
}

.social-media a {
    display: inline-block;
    margin-right: 10px;
    color: #4CAF50;
    text-decoration: none;
}

.social-media a:hover {
    text-decoration: underline;
}

.map iframe {
    width: 100%;
    border: 0;
    border-radius: 5px;
}

footer {
    background-color: #4CAF50;
    color: white;
    text-align: center;
    padding: 10px;
    position: fixed;
    width: 100%;
    bottom: 0;
}

    </style>
</head>
<body>
    <header>
        <h1>Contact Us</h1>
    </header>
    <main>
        <section class="contact-form">
            <h2>Get in Touch</h2>
            <form action="submit_form.php" method="POST">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                
                <label for="message">Message:</label>
                <textarea id="message" name="message" rows="4" required></textarea>
                
                <button type="submit">Send</button>
            </form>
        </section>
        
        <section class="contact-info">
            <h2>Our Contact Information</h2>
            <p><strong>Phone:</strong> (123) 456-7890</p>
            <p><strong>Email:</strong> info@example.com</p>
            <p><strong>Address:</strong> 123 Main Street, Hometown, USA</p>
            
            <div class="social-media">
                <a href="https://facebook.com" target="_blank">Facebook</a>
                <a href="https://twitter.com" target="_blank">Twitter</a>
                <a href="https://linkedin.com" target="_blank">LinkedIn</a>
            </div>
        </section>
        
        <section class="map">
            <h2>Find Us</h2>
            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3153.221068342209!2d-122.41941568468164!3d37.77492927975859!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8085808a353a98d7%3A0x1b07f5c1b6e7ed27!2sSan%20Francisco%2C%20CA%2094181%2C%20USA!5e0!3m2!1sen!2sin!4v1639452687780!5m2!1sen!2sin" 
                    width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
        </section>
    </main>
    <footer>
        <p>&copy; 2024 Your Company Name. All rights reserved.</p>
    </footer>
</body>
</html>

'''

    return HttpResponse(cont)