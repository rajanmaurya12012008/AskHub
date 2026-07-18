// AskHub Javascript Interactions
document.addEventListener('DOMContentLoaded', () => {

    // 1. Auto-dismiss Flash Messages after 5 seconds
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach((message) => {
        // Dismiss button handler
        const closeBtn = message.querySelector('.flash-close');
        if (closeBtn) {
            closeBtn.addEventListener('click', () => {
                dismissMessage(message);
            });
        }
        
        // Auto dismiss timer
        setTimeout(() => {
            dismissMessage(message);
        }, 5000);
    });

    function dismissMessage(element) {
        element.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        element.style.opacity = '0';
        element.style.transform = 'translateY(-10px)';
        setTimeout(() => {
            element.remove();
        }, 500);
    }

    // 2. Client Side Form Validations
    const signupForm = document.querySelector('#signupForm');
    if (signupForm) {
        signupForm.addEventListener('submit', (e) => {
            const password = document.querySelector('#password').value;
            const confirmPassword = document.querySelector('#confirm_password').value;
            
            if (password.length < 6) {
                e.preventDefault();
                alert('Password must be at least 6 characters long!');
                return;
            }

            if (password !== confirmPassword) {
                e.preventDefault();
                alert('Passwords do not match!');
                return;
            }
        });
    }

    const askForm = document.querySelector('#askForm');
    if (askForm) {
        askForm.addEventListener('submit', (e) => {
            const title = document.querySelector('#title').value.trim();
            const description = document.querySelector('#description').value.trim();

            if (title.length < 10) {
                e.preventDefault();
                alert('Question title must be at least 10 characters long.');
                return;
            }

            if (description.length < 20) {
                e.preventDefault();
                alert('Question description must be at least 20 characters long.');
                return;
            }
        });
    }

    const answerForm = document.querySelector('#answerForm');
    if (answerForm) {
        answerForm.addEventListener('submit', (e) => {
            const content = document.querySelector('#content').value.trim();

            if (content.length < 5) {
                e.preventDefault();
                alert('Answer content matches too short! (Minimum 5 characters)');
                return;
            }
        });
    }

    // 3. User Profile Tab Switching Logic
    const profileTabs = document.querySelectorAll('.tab-btn');
    if (profileTabs.length > 0) {
        const questionsList = document.querySelector('#my-questions');
        const answersList = document.querySelector('#my-answers');

        profileTabs.forEach(tab => {
            tab.addEventListener('click', () => {
                // Remove active class from all tabs
                profileTabs.forEach(t => t.classList.remove('active'));
                tab.classList.add('active');

                // Toggle visibility based on the active tab target
                const target = tab.dataset.target;
                if (target === 'questions') {
                    questionsList.style.display = 'block';
                    answersList.style.display = 'none';
                } else if (target === 'answers') {
                    questionsList.style.display = 'none';
                    answersList.style.display = 'block';
                }
            });
        });
    }
});
