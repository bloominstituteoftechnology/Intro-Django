import React, { Component } from 'react'
import axios from 'axios'

class Login extends Component {
  state = {
    username: '',
    password: '',
  }

  render() {
    return (
      <form onSubmit={this.formSubmitHandler}>
        <div>
          <label>Username</label>
          <input
            value={this.state.username}
            onChange={this.inputChangeHandler}
            name="username"
            type="text"
          />
        </div>

        <div>
          <label>password</label>
          <input
            value={this.state.password}
            onChange={this.inputChangeHandler}
            name="password"
            type="password"
          />
        </div>

        <div>
          <button type="submit">Signin</button>
        </div>
      </form>
    )
  }
  formSubmitHandler = event => {
    event.preventDefault()
    console.log('I am here submit handler')
    axios
      .post('http://localhost:8000/admin/login/', this.state)
      .then(response => {
        console.log('response data', response.data)
        localStorage.setItem(response.data.token)
        console.log(localStorage)
      })
      .catch(err => console.error(err.message))
  }

  inputChangeHandler = event => {
    const { name, value } = event.target
    this.setState({ [name]: value })
  }
}
export default Login
