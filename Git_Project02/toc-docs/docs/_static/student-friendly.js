// Ultra-minimal JavaScript for student support

document.addEventListener('DOMContentLoaded', function() {
    
    // Progress tracking
    function updateProgress() {
        const totalSections = 4; // basics, automata, languages, complexity
        const completed = JSON.parse(localStorage.getItem('toc-progress') || '[]');
        const percentage = (completed.length / totalSections) * 100;
        
        const progressBar = document.getElementById('progress-fill');
        const progressText = document.getElementById('progress-text');
        
        if (progressBar) {
            progressBar.style.width = percentage + '%';
        }
        if (progressText) {
            progressText.textContent = Math.round(percentage) + '% Complete';
        }
    }
    
    // Mark section complete
    window.markComplete = function(section) {
        let completed = JSON.parse(localStorage.getItem('toc-progress') || '[]');
        if (!completed.includes(section)) {
            completed.push(section);
            localStorage.setItem('toc-progress', JSON.stringify(completed));
            updateProgress();
            showEncouragement();
        }
    };
    
    // Show encouragement message
    function showEncouragement() {
        const messages = [
            "Great job! Keep going! 🌟",
            "You're doing amazing! 💪", 
            "Excellent progress! 🎉",
            "You've got this! 🚀"
        ];
        
        const message = messages[Math.floor(Math.random() * messages.length)];
        
        // Create temporary notification
        const notification = document.createElement('div');
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: #10b981;
            color: white;
            padding: 1rem 1.5rem;
            border-radius: 8px;
            z-index: 1000;
            animation: slideIn 0.3s ease;
        `;
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.remove();
        }, 3000);
    }
    
    // Help toggle functionality
    window.toggleHelp = function(helpId) {
        const helpContent = document.getElementById(helpId);
        if (helpContent) {
            helpContent.style.display = 
                helpContent.style.display === 'none' ? 'block' : 'none';
        }
    };
    
    // Initialize progress on page load
    updateProgress();
    
    // Add CSS animation for notifications
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideIn {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
    `;
    document.head.appendChild(style);
});
