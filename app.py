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
      'url': '/sqe',
      'button_text': 'Try Now !!'
    },
    {
      'id': 2,
      'title': 'Business Analyst Agent',
      'description': 'An AI Agent that creates stories for given business requirements',
      'color': 'from-green-500 to-green-600',
      'icon_svg': """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-headphones"><path d="M3 14h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-7a9 9 0 0 1 18 0v7a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3"/><path d="M18 14V6"/></svg>""",
      'button_text': 'Try Now !!'
    },
    {
      'id': 3,
      'title': 'Marketing Content Creator',
      'description': 'Generates creative and engaging copy for social media posts, email campaigns, and blog articles. Supports various tones and styles.',
      'color': 'from-purple-500 to-purple-600',
      'icon_svg': """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-pencil"><path d="M17 3a2.85 2.83 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5Z"/></svg>""",
      'button_text': 'Coming soon !!'
    },
    {
      'id': 4,
      'title': 'Data Analyst AI',
      'description': 'Analyzes large datasets to find patterns, generate insights, and create automated reports for business intelligence.',
      'color': 'from-yellow-500 to-yellow-600',
      'icon_svg': """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-pie-chart"><path d="M21.21 15.89A10 10 0 1 1 8 2.83"/><path d="M22 12A10 10 0 0 0 12 2v10z"/></svg>""",
      'button_text': 'Coming soon !!'
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
        <div class="p-4 flex flex-col items-center">
          <h3 class="text-xl font-semibold text-gray-900 mb-2">{{ agent.title }}</h3>
          <p class="text-sm text-gray-600 mb-4 line-clamp-2 h-[40px]">{{ agent.description }}</p>
          <!-- Using an anchor tag for the button with a conditional href and target -->
          <a {% if agent.url and agent.button_text == "Try Now !!" %} href="{{ agent.url }}" target="_blank" {% endif %} class="inline-block text-center bg-gray-900 text-white font-medium py-1 px-2 rounded-xl hover:bg-gray-700 transition-colors duration-300 transform hover:scale-105 active:scale-95 shadow-md text-sm">
            {{ agent.button_text }}
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

# The HTML template as a multi-line string.
# This includes all the HTML, Tailwind CSS, and JavaScript from your design.
sqe_agent_html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quality Engineer Agent</title>
    <!-- Tailwind CSS for a clean, modern look -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        body { font-family: 'Inter', sans-serif; }
    </style>
</head>
<body class="bg-gray-100 flex flex-col min-h-screen">

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
                <h1 class="text-xl font-bold text-gray-900">Quality Engineer Agent</h1>
            </div>
            <!-- An empty div to maintain spacing and alignment on the right side of the header -->
            <div class="flex items-center"></div>
        </div>
    </header>

    <!-- Main Content Area -->
    <main class="flex-grow container mx-auto px-4 py-8 md:py-12 flex items-center justify-center">
        <div class="bg-gradient-to-r from-blue-100 to-white rounded-2xl shadow-lg p-8 max-w-4xl w-full">
            <form id="agentForm" class="space-y-4">
                <!-- Top Section: Tell me what to do -->
                <div class="border-2 border-blue-500 rounded-lg p-4 shadow-sm bg-white">
                    <div>
                        <label for="textField" class="block text-sm font-medium text-gray-700 mb-1">Tell me what to do (e.g., Analyze JIRA Issue# TP-3)</label>
                        <input
                            type="text"
                            id="textField"
                            name="textField"
                            placeholder="Type something here..."
                            class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                        >
                    </div>
                </div>

                <!-- Bottom Section: Optional fields -->
                <div class="border-2 border-blue-500 rounded-lg p-4 shadow-sm bg-white">
                    <div class="grid grid-cols-3 gap-4">
                        <div>
                            <label for="jiraUrl" class="block text-sm font-medium text-gray-700 mb-1">JIRA URL (Optional)</label>
                            <input
                                type="text"
                                id="jiraUrl"
                                name="jiraUrl"
                                placeholder="https://your-jira-instance.com"
                                class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                            >
                        </div>
                        <div>
                            <label for="jiraUserName" class="block text-sm font-medium text-gray-700 mb-1">JIRA User Name (Optional)</label>
                            <input
                                type="text"
                                id="jiraUserName"
                                name="jiraUserName"
                                placeholder="Enter your JIRA username"
                                class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                            >
                        </div>
                        <div>
                            <label for="jiraToken" class="block text-sm font-medium text-gray-700 mb-1">JIRA Token (Optional)</label>
                            <input
                                type="text"
                                id="jiraToken"
                                name="jiraToken"
                                placeholder="Enter your JIRA API token"
                                class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                            >
                        </div>
                        <div>
                            <label for="githubHost" class="block text-sm font-medium text-gray-700 mb-1">GitHub Host (Optional)</label>
                            <input
                                type="text"
                                id="githubHost"
                                name="githubHost"
                                placeholder="e.g., github.com or github.mycompany.com"
                                class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                            >
                        </div>
                        <div>
                            <label for="githubToken" class="block text-sm font-medium text-gray-700 mb-1">GitHub Token (Optional)</label>
                            <input
                                type="text"
                                id="githubToken"
                                name="githubToken"
                                placeholder="Enter your GitHub personal access token"
                                class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                            >
                        </div>
                        <div>
                            <label for="githubRepoName" class="block text-sm font-medium text-gray-700 mb-1">GitHub Repository (Optional)</label>
                            <input
                                type="text"
                                id="githubRepoName"
                                name="githubRepoName"
                                placeholder="e.g., my-repo"
                                class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                            >
                        </div>
                    </div>
                </div>

                <button
                    type="submit"
                    class="block mx-auto bg-gray-900 text-white py-0.5 px-2 rounded-md hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-gray-900 focus:ring-offset-2 transition-colors duration-300 font-medium text-sm"
                >
                    Start Running
                </button>
            </form>

            <!-- Message Display Area -->
            <div id="messageArea" class="mt-4 text-center text-sm font-medium text-gray-700 hidden">
                The code analysis will take sometime, so please be patient !!
            </div>
        </div>
    </main>

    <!-- Footer Section -->
    <footer class="bg-gray-800 text-white py-6">
        <div class="container mx-auto px-4 flex justify-between items-center">
            <p>&copy; 2025 HCL Technologies. All rights reserved.</p>
            <p class="text-base font-bold italic text-white">Powered by Engineering and R&D Services</p>
        </div>
    </footer>

    <script>
        document.getElementById('agentForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            const textFieldValue = document.getElementById('textField').value;
            const baseUrl = 'https://piglet-becoming-gar.ngrok-free.app';

            // Get the message area element
            const messageArea = document.getElementById('messageArea');

            // Show the message
            messageArea.classList.remove('hidden');

            // Constructing the URL with query parameters
            const url = new URL(baseUrl);
            url.searchParams.append('query', textFieldValue);
            url.searchParams.append('goponsobdo', 'amijantechai');

            console.log('Opening URL in same window:', url.toString());

            // Open the URL in the same window
            window.open(url.toString(), '_self');

            // Optionally hide the message after a short delay
            setTimeout(() => {
                messageArea.classList.add('hidden');
            }, 3000); // Hide after 3 seconds
        });
    </script>
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

@app.route('/sqe')
def sqehome():
    """
    This route renders the main page of the Software Quality Agent.
    """
    return render_template_string(sqe_agent_html_template)

if __name__ == '__main__':
    # Running the Flask app in debug mode for development.
    # In a production environment, you would use a more robust server.
    app.run(debug=True)
