<?php

session_start();


$uname = $_POST['uname'];
$pwd = $_POST['pwd'];
$mail = $_POST['mail'];

if (!empty($uname) || !empty($pwd) || !empty($mail)){

	$conn = new mysqli("localhost","root","","register");

	if ($conn -> connect_errno) {
  		echo "Failed to connect to MySQL: " . $conn -> connect_error;
  		exit();
	}
	else
	{
		$SELECT = "SELECT mail FROM user_registration where mail = ? Limit 1";
		$INSERT = "INSERT INTO user_registration(uname,pwd,mail) values(?,?,?)";

		$stmt = $conn->prepare($SELECT);
		$stmt->bind_param("s",$mail);
		$stmt->execute();
		$stmt->bind_result($mail);
		$stmt->store_result();
		$rnum = $stmt->num_rows;

		if($rnum==0){
			$stmt->close();
			$stmt = $conn->prepare($INSERT);
			$stmt->bind_param("sss",$uname,$pwd,$mail);
			$stmt->execute();
			header('location:Login.html');
		}
		else{
			echo '<script>alert("Someone already registered this email")</script>';
		}
		$stmt->close();
	}
	}
else{
	echo "All field are required";
	die();
}
?>