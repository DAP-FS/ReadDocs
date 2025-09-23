Welcome to Educational Documentation
====================================

.. raw:: html

   <div class="welcome-banner">
     <h2>Start Your Learning Journey</h2>
     <p>This documentation is designed especially for students who need extra support and want to learn at their own pace.</p>
   </div>

Learning Pathways
-----------------

Choose your starting point based on your current knowledge level:

.. raw:: html

   <div class="pathway-cards">
     <div class="pathway-card beginner">
       <h3>👶 Beginner</h3>
       <p><strong>New to the topic?</strong></p>
       <p>Start with Getting Started → Chapter 1 → Chapter 2</p>
       <p><em>Estimated time: 6-8 hours</em></p>
       <button onclick="localStorage.setItem('pathway', 'beginner')" class="pathway-btn">Choose Beginner Path</button>
     </div>
     
     <div class="pathway-card intermediate">
       <h3>📚 Intermediate</h3>
       <p><strong>Some experience?</strong></p>
       <p>Start with Chapter 2 → Chapter 3 → Advanced exercises</p>
       <p><em>Estimated time: 4-6 hours</em></p>
       <button onclick="localStorage.setItem('pathway', 'intermediate')" class="pathway-btn">Choose Intermediate Path</button>
     </div>
     
     <div class="pathway-card advanced">
       <h3>🚀 Advanced</h3>
       <p><strong>Ready for challenges?</strong></p>
       <p>Jump to Chapter 3 → Instructor Notes → Projects</p>
       <p><em>Estimated time: 2-4 hours</em></p>
       <button onclick="localStorage.setItem('pathway', 'advanced')" class="pathway-btn">Choose Advanced Path</button>
     </div>
   </div>

.. raw:: html

   <div class="progress-container">
     <h3>Your Progress</h3>
     <div class="progress-bar">
       <div class="progress-fill" id="overall-progress"></div>
     </div>
     <p class="progress-text" id="progress-text">0% Complete</p>
   </div>

Table of Contents
-----------------

.. toctree::
   :maxdepth: 2
   :caption: Learning Materials:

   chapters/getting-started
   chapters/chapter1
   chapters/chapter2  
   chapters/chapter3
   chapters/glossary
   chapters/instructor-notes

How to Use This Documentation
-----------------------------

✨ **For Students:**

- Each chapter has **Learning Objectives** at the top
- Look for **💡 Tip** and **⚠️ Important** boxes
- Click **"Show Hint"** buttons when stuck
- Use **"Mark Complete"** to track your progress
- Videos are marked with **🌐 International UI** for accessibility

📖 **Navigation Tips:**

- Use the **sidebar** to jump between chapters
- **Search** using the magnifying glass icon
- **Previous/Next** buttons are at the bottom of each page
- Press **"k"** to open keyboard shortcuts

🎯 **Learning Features:**

- **Progressive hints** - get help without seeing full solutions
- **Self-paced markers** - track what you've completed  
- **Accessibility** - larger fonts, clear contrast, keyboard navigation
- **Mobile-friendly** - works on tablets and phones

Need Help?
----------

.. admonition:: If You're Stuck
   :class: tip

   1. **Read the summary** at the top of each chapter
   2. **Try the hints** - they give step-by-step guidance
   3. **Check the glossary** for definitions
   4. **Review prerequisites** listed in each chapter
   5. **Take breaks** - learning takes time!

.. raw:: html

   <div class="help-video">
     <h3>🌐 International UI: Getting Started Video</h3>
     <button class="video-btn" onclick="openVideo('getting-started')">
       ▶️ Watch Getting Started Guide (5 min)
     </button>
   </div>

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
