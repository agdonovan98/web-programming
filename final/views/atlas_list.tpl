<!-- table layout -->
<!DOCTYPE html>
<html>
<body>
    <table class="table table-light table-bordered table-hover">
        <tr>
            <th>#</th>
            <th>Location</th>
            <th>Date</th>
            <th>Comments</th>
            <th>Edit</th>
            <th>Delete</th>
        </tr>
        %for item in items:
            <tr>
                <th>{{item['id']}}</th>
                <td>{{item['place']}}</td>
                <td>{{item['date']}}</td>
                <td>{{item['comments']}}</td>
                <td>
                    <a href="/edit/{{item['id']}}">
                        <span class="material-icons">
                           edit
                        </span>
                    </a>
                </td>
                <td>
                    <a href="/delete/{{item['id']}}">
                        <span class="material-icons">
                            delete
                        </span>
                    </a>
                </td>
            </tr>
        %end
    </table>
    <hr/>
    <a href="insert">
        <span class="material-icons md-24">add</span>Add new location
    </a>
    <hr/>      
    <script>
    $(document).ready(function() {
        $('.msg').hide()
    });
    </script>
</body>
</html>