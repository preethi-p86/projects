<!DOCTYPE html>
<html>
<head>
	<title> QUIZ BUZZ DASHBOARD </title>
	<style>
		body{background: center/cover url("simple.jpg");}

		table{
			border-collapse: collapse;
			width: 100%;
			color: #d96459;
			font-family: monospace;
			font-size: 25px;
			text-align: left;
		}
		th{
			background-color: #d96459;
			color: white;
		}
	</style>
</head>
<body>
<table>
	<tr>
		<th>NAME</th>
		<th>CATEGORY_TYPE</th>
		<th>SCORE</th>
	</tr>
	<?php
	$conn =mysqli_connect("localhost","root","","register");
	if($conn-> connect_error){
		die("connection failed:".$conn-> connect_error);
	}
	$sql ="SELECT User_Name, Category_Type, Max(User_Score) as User_Score FROM user_score_table GROUP BY Category_Type,Mail_ID having User_Score>50 order by Category_Type ASC";
	$result = $conn-> query($sql);

	if($result-> num_rows >0){
		while($row = $result-> fetch_assoc()){
			echo "<tr><td>".$row["User_Name"]."</td><td>". $row["Category_Type"] ."</td><td>".$row["User_Score"]."</td></tr>";
		}
		echo "</table>";
	}
	else{
		echo "0 result";
	}
	$conn->close();
	?>
</table>
</body>
</html>

