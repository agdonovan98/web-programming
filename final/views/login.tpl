<!-- page for returning users to log in -->
<html>
    <head>
        %include header
    </head>
    <h2>Login</h2>
    <p>If you've already registered with us, fill out the forms below to access your Atlas.</p><br>
    <form action="/login" method="post">
        Username<br/>
        <input type="text" name="username"/><br/>
        Password<br/>
        <input type="password" name="password"/><br/>
        <hr/>
        <input type="submit" value="Login"/>
    </form>
</html>