# app.py
from flask import Flask, render_template_string

app = Flask(__name__)

# Mock data for the AI agents. In a real application, this would come from an API or database.
agents_data = [
    {
      'id': 1,
      'title': 'Quality Engineer Agent',
      'description': 'An AI agent designed to triage and then implement code fixes to resolve Issues.',
      'color': 'from-blue-500 to-blue-600',
      'icon_svg': """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-code"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>""",
      'url': 'https://www.google.com'
    },
    {
      'id': 2,
      'title': 'Business Analyst Agent',
      'description': 'An AI Agent that creates stories for given business requirements',
      'color': 'from-green-500 to-green-600',
      'icon_svg': """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-headphones"><path d="M3 14h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-7a9 9 0 0 1 18 0v7a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3"/><path d="M18 14V6"/></svg>"""
    },
    {
      'id': 3,
      'title': 'Marketing Content Creator',
      'description': 'Generates creative and engaging copy for social media posts, email campaigns, and blog articles. Supports various tones and styles.',
      'color': 'from-purple-500 to-purple-600',
      'icon_svg': """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-pencil"><path d="M17 3a2.85 2.83 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5Z"/></svg>"""
    },
    {
      'id': 4,
      'title': 'Data Analyst AI',
      'description': 'Analyzes large datasets to find patterns, generate insights, and create automated reports for business intelligence.',
      'color': 'from-yellow-500 to-yellow-600',
      'icon_svg': """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-pie-chart"><path d="M21.21 15.89A10 10 0 1 1 8 2.83"/><path d="M22 12A10 10 0 0 0 12 2v10z"/></svg>"""
    },
]

# The HTML template as a multi-line string.
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AI Agent Portfolio</title>
  <!-- Tailwind CSS CDN for styling -->
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    body {
      font-family: 'Inter', sans-serif;
    }
  </style>
</head>
<body class="min-h-screen bg-gray-50 font-sans antialiased text-gray-800">

  <!-- Header Section -->
  <header class="sticky top-0 bg-white/80 backdrop-blur-md z-50 shadow-sm">
    <div class="container mx-auto px-4 py-4 md:py-6 flex flex-col md:flex-row items-center justify-between">
      <!-- Logo on the left -->
      <div class="flex items-center space-x-4 mb-4 md:mb-0">
        <!-- HCLTech Logo - Sourced from a public domain SVG on Wikimedia Commons for reliability -->
        <img
          src="https://www.hcltech.com/themes/custom/hcltech/images/hcltech-new-logo.svg"
          alt="HCLTech Logo"
          class="h-5 md:h-6"
        />
      </div>
      <!-- Title centered in the middle -->
      <div class="flex-grow flex justify-center mb-4 md:mb-0">
        <h1 class="text-3xl font-bold text-gray-900">AI Agent Portfolio</h1>
      </div>
      <!-- An empty div to maintain spacing and alignment on the right side of the header -->
      <div class="flex items-center"></div>
    </div>
  </header>

  <!-- Main Content Area -->
  <main class="container mx-auto px-4 py-2 md:py-4">
    <section class="mb-6">
      <h2 class="text-3xl font-bold text-gray-900 mb-2">Explore AI Agents</h2>
      <p class="text-lg text-gray-600 max-w-5xl">
        Discover a wide range of AI agents designed to automate tasks, improve efficiency, and enhance your business operations.
      </p>
    </section>

    <!-- Agent List -->
    {% if agents %}
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 place-items-center">
      <!-- Jinja2 loop to iterate over the agents data passed from app.py -->
      {% for agent in agents %}
      <div class="bg-white rounded-2xl shadow-lg hover:shadow-xl transition-shadow duration-300 overflow-hidden w-full max-w-xl">
        <!-- The icon will be a placeholder since we can't use React components directly -->
        <div class="p-1 bg-gradient-to-br {{ agent.color }} text-white flex items-center justify-center rounded-t-2xl">
          {{ agent.icon_svg | safe }}
        </div>
        <div class="p-4">
          <h3 class="text-xl font-semibold text-gray-900 mb-2">{{ agent.title }}</h3>
          <p class="text-sm text-gray-600 mb-4 line-clamp-2 h-[40px]">{{ agent.description }}</p>
          <!-- Using an anchor tag for the button with a conditional href and target -->
          <a {% if agent.url %} href="{{ agent.url }}" target="_blank" {% endif %} class="block text-center w-full bg-gray-900 text-white font-medium py-2 rounded-xl hover:bg-gray-700 transition-colors duration-300 transform hover:scale-105 active:scale-95 shadow-md text-sm">
            Try Now !!
          </a>
        </div>
      </div>
      {% endfor %}
    </div>
    {% else %}
    <div class="text-center p-12 bg-white rounded-2xl shadow-lg">
      <p class="text-xl text-gray-600 font-semibold">No agents found.</p>
    </div>
    {% endif %}
  </main>

  <!-- Footer Section -->
  <footer class="bg-gray-800 text-white py-6">
    <div class="container mx-auto px-4 flex justify-between items-center">
      <p>&copy; 2025 HCL Technologies. All rights reserved.</p>
      <p class="text-base font-bold italic text-white">Powered by Engineering and R&D Services</p>
    </div>
  </footer>
</body>
</html>
"""

@app.route('/')
def home():
    """
    This route renders the main page of the AI Agent Portfolio.
    It passes the list of agents to the HTML template for rendering.
    """
    return render_template_string(html_template, agents=agents_data)

if __name__ == '__main__':
    # Running the Flask app in debug mode for development.
    # In a production environment, you would use a more robust server.
    app.run(debug=True)
