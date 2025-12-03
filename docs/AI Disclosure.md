Many moons have passed since my last update on this AI Disclosure for the reason of I have been mainly using API docs and W3 schools and other online resources to try and piece together my password vault. I have now primarily been using ChatGPT to troubleshoot my errors and ask it for resources where I can find the answers instead of just asking it "How do I do this?".

I asked ChatGPT 

<aside>

“I'm trying to get my navigation bar to have the user off to the right and my 3 other links stay to the left. How can I do that?”

</aside>

ChatGPT responded:

<aside>

You can easily do this with **CSS flexbox**. Here’s a simple example:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Navbar Example</title>
  <style>
    /* Navbar container */
    nav {
      display: flex;                 /* Use flexbox */
      justify-content: space-between; /* Space between left and right sides */
      align-items: center;           /* Vertically center items */
      background-color: #333;
      padding: 10px 20px;
      color: white;
    }

    /* Left links group */
    .nav-links {
      display: flex;
      gap: 20px; /* spacing between links */
    }

    .nav-links a {
      color: white;
      text-decoration: none;
    }

    .nav-links a:hover {
      text-decoration: underline;
    }

    /* Right user section */
    .user {
      font-weight: bold;
    }
  </style>
</head>
<body>
  <nav>
    <div class="nav-links">
      <a href="#">Home</a>
      <a href="#">About</a>
      <a href="#">Contact</a>
    </div>
    <div class="user">
      Hello, User
    </div>
  </nav>
</body>
</html>
```

### 🔍 Explanation

- `display: flex` makes the `<nav>` container flexible.
- `justify-content: space-between` pushes the first group (`.nav-links`) to the **left** and the second (`.user`) to the **right**.
- You can group the left links in a `<div>` so they stay together.
</aside>

I kept going back and forth tweaking little things here and there because the Nav bar wouldn’t align the user to the right, ChatGPT suggested I hit Ctrl + Shift + R to hard refresh and that worked. It updated to how I wanted.
I also did not use all of the code ChatGPT sent me, just took bits and pieces.

