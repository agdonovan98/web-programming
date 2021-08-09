<!-- form for inserting locations -->
<html>
    <head>
        %include header
    </head>
    <body>
        <h2>Add Location</h2>
        <p>Fill out the forms below to add a new location to your Atlas!</p><br>
        <form action="/insert" method="post">
            Location<br>
            <input type="text" name="place"/><br/>
            Date<br>
            <input type="text" name="date"/><br/>
            Comments<br>
            <input type="text" name="comments"/><br/>
            <hr/>
            <button onclick="window.location='/'; return false">Cancel</button>&nbsp
            <input type="submit" value="Submit"/>
        </form>
        <hr/>
        <p>Need help finding a place? Use this map!</p>
        <iframe src="https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d7145.717103985639!2d-81.34406355555672!3d41.14753615454222!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2sus!4v1628470954111!5m2!1sen!2sus" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
    </body>
</html>