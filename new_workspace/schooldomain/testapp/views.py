from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def mysite(request):
    site ='''
    <style>
        p{
          font-weight:bold;
          margin-left: 20px;
          margin-right:20px;
          font-size:18px;
        }
    </style>
    <h1 align="center" style="color:blue">Sagar Group of Institution</h1>
    <p>Sagar Institute of Science and Technology (SISTec®), established in the year 2007, is one of the best engineering colleges, located in the heart of the state, the city of lakes - Bhopal. SISTec is the brand name for technical colleges under the umbrella of the Sagar Group of Institutions®. Boasting state-of-the-art facilities, a diverse student body, and a talented pool of faculty, SISTec has established itself as a leader in providing quality education offering B.Tech., Management, and M.Tech. programs. The academic programs are designed to meet the needs and interests of students from all backgrounds, making SISTec the perfect place to jumpstart your future. The brand has a strong motivation towards innovation in curriculum implementation. It further aspires to be a part of the education revolution in Technical education, impacting futuristic technologies in the Indian framework. In this process, it aims to be one of the finest providers of technical education in India.</p>
    <br>
    <h2 align = "center" style="color:red">Engineering</h2>
    <p>The B.Tech. Engineering Program at Sagar Institute of Science and Technology (SISTec) Gandhi Nagar Campus is developed from an industrial point of view, with a great focus on modern technologies employed in the industries. Engineers are the focal point in our economy to design, test, and develop the next generation of products and services for the betterment of society. In this regard, the pedagogy is designed based on industry-oriented training modules a level extra than the standard university curriculum. Similarly, the MTech Engineering Program is developed from a research point of view to inculcate the spirit of innovation and development in Science & Technology.</p>
    <br>
    <h3>B-Tech</h3>
    <ul>
        <li>Civil Engineering</li>
        <li>Computer Science & Engineering</li>
        <li>Computer Science & Information Technology</li>
        <li>CSE with Artificial Intelligence and Data Science</li>
        <li>CSE with Cyber Security</li>
        <li>Electrical & Electronics Engineering</li>
        <li>Electronics & Communication Engineering</li>
        <li>Mechanical Engineering</li>
    </ul>
    <br>
    <h3>M-Tech</h3>
    <ul>
        <li>Computer Science & Engineering</li>
        <li>Digital Communication</li>
        <li>Machine Design</li>
        <li>Structural Engineering</li>
        <li>Thermal Power & Engineering</li>
        <li>Very-Large-Scale Integration (VLSI) Design</li>
    </ul>
'''
    return HttpResponse(site)