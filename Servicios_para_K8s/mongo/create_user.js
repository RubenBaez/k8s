db.createUser(
    {
      user: "ruben",
      pwd: "1234",
      roles: [
         { role: "readWrite", db: "jsondb" }
      ]
    }
);
