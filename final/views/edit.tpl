<!-- form for editing locations -->
<!DOCTYPE html>
<html>
    <head>
        %include header
    </head>
    <body>
        <h2>Edit Location</h2><br>
        <form action="/edit" method="post">
            Location<br> 
            <input type="text" name="place" value="{{item['place']}}"/><br>
            Date<br> 
            <input type="text" name="date" value="{{item['date']}}"/><br>
            Comments<br> 
            <input type="text" name="comments" value="{{item['comments']}}"/><br>
            <hr/>
            <button onclick="window.location='/'; return false">Cancel</button>&nbsp
            <input type="submit" value="Submit"/>
            <input type="text" name="id" value="{{item['id']}}" readonly hidden/>
        </form>
        <hr/>
    </body>
</html>