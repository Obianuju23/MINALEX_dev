async function submitForm(formId) {
    let email = document.getElementById(formId).querySelector('input[name="email"]').value;
    let password = document.getElementById(formId).querySelector('input[name="password"]').value;

    let formData = {
        "email": email,
        "password": password
    };

    // Check which form is being submitted
    if (formId === 'loginForm') {
        // Handle login form submission
        console.log("Login Form Submission:", formData);
        // Make AJAX request to the backend for login
        const url = 'http://localhost:5000/login/user';  // Corrected URL

        try {
            const response = await fetch(url, {
                method: 'POST',
                body: JSON.stringify(formData),
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            // Check if the response is in JSON format
            const contentType = response.headers.get('content-type');
            if (contentType && contentType.includes('application/json')) {
                const responseData = await response.json();
                console.log('Success:', responseData);
            } else {
                console.log('Success:', response);  // Log the non-JSON response
            }

            // Redirect only after successful response
            // window.location.href = '/success';

        } catch (error) {
            console.error('Error:', error);
        }

    } else if (formId === 'registerForm') {
        // Handle register form submission
        console.log("Register Form Submission:", formData);
        // Make AJAX request to the backend for registration
    } else if (formId === 'forgotPasswordForm') {
        // Handle forgot password form submission
        console.log("Forgot Password Form Submission:", formData);
        // Make AJAX request to the backend for password reset
    }
}
