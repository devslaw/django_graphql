API Endpoints
========


## Mutations

### Registration
```
mutation {
  registerUser(input: {
    email: "support@devslaw.com",
    password: "devslaw",
    firstName: "Devslaw",
    lastName: "Devslaw LLC"
  }) {
    ok,
    user {
      id,
      firstName,
      email,
      token
    }
  }
}
```

### Log In
Log in to get a JWT for future requests.
```
mutation {
  loginUser(input: {
    email: "support@devslaw.com",
    password: "devslaw"
  }) {
    ok,
    user {
      id,
      firstName,
      email,
      token
    }
  }
}
```

### Reset Password
First send a password reset request with this mutation:
```
mutation {
  resetPasswordRequest(input: {
    email: "support@devslaw.com"
  }) {
    ok
  }
}
```

### Edit User Data
```
mutation{
  editUser(editUserData:{id:"11",firstName:"devslaw",lastName:"devslaw LLC",email:"support@devslaw.com"}){
     ok
   }
}
```

### Add User
```
mutation{
  addUser(addUserData:{firstName:"devslaw",lastName:"devslaw LLC",email:"support@devslaw.com"}){
    user{
      username
    }
  }
}
```
