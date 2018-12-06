import React from 'react'
import styled from 'styled-components'

class Login extends React.Component {
  state = {
    username: "",
    password: "",
  }

  handleChange = (e) => {
    this.setState({
      [e.target.name]: e.target.value
    })
  }

  handleSubmit = (e) => {
    e.preventDefault()
    this.props.login({
      username: this.state.username,
      password: this.state.password
    })
    this.setState({
      username: "",
      password: ""
    })
  }

  render() {
    return (
      <Form1 onSubmit={this.handleSubmit}>
        <Label>
          <Input
            name="username"
            type="text"
            placeholder="👤 username"
            onChange={this.handleChange}
            value={this.state.username}
          />
        </Label>
        <Label>
          <Input
            name="password"
            type="password"
            placeholder="🔑 password"
            onChange={this.handleChange}
            value={this.state.password}
          />
        </Label>
        <Button
          type="submit"
        >
          Submit
        </Button>
      </Form1>
    )
  }
}

const Form1 = styled.form`
  background: white;
  display: flex;
  flex-direction: column;
  border: none;
  border-radius: 5px;
  box-shadow: 0 0 10px black;
  padding: 1rem;
`
const Label = styled.label`
  margin: 1rem;
`
const Input = styled.input`
  border-radius: 2px;
  padding: 5px;
  font-size: 16px;
  text-align: center;
  margin: 0 1rem;
  box-shadow: 0 2px 2px gray;
  border: none;
`
const Button = styled.button`
  width: 50%;
  margin: 1rem auto;
  background: #61DAFB;
  padding: 5px;
  font-size: 16px;
  border-radius: 2px;
  border: none;
  box-shadow: 0 2px 2px gray;
  &:hover {
    cursor: pointer;
  }
`

export default Login
