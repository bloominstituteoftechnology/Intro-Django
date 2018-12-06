import React from 'react'
import styled from 'styled-components'

class CountryForm extends React.Component {
  state = {
    country: "",
    capital: "",
    wiki: "",
    visited: false
  }

  handleChange = (e) => {
    if (e.target.name === "visited") {
      this.setState({ visited: !this.state.visited })
    }
    else {
      this.setState({
        [e.target.name]: e.target.value
      })
    }
  }

  handleSubmit = (e) => {
    e.preventDefault()
    const newCountry = {
      "country": this.state.country,
      "capital": this.state.capital,
      "wiki": this.state.wiki,
      "visited": this.state.visited
    }
    this.props.addCountry(newCountry)
    this.props.toggleCreate(e)
    this.setState({
      country: "",
      capital: "",
      wiki: "",
      visited: false
    })
  }

  render() {
    return (
      <Form1 onSubmit={this.handleSubmit}>
        <Label>
          <Input
            name="country"
            type="text"
            placeholder="🌐 country"
            onChange={this.handleChange}
            value={this.state.country}
          />
        </Label>
        <Label>
          <Input
            name="capital"
            type="text"
            placeholder="📌 capital"
            onChange={this.handleChange}
            value={this.state.capital}
          />
        </Label>
        <Label>
          <Input
            name="wiki"
            type="text"
            placeholder="𝘞 wikipedia"
            onChange={this.handleChange}
            value={this.state.wiki}
          />
        </Label>
        <Label>
          Visited:
          <Input
            name="visited"
            type="checkbox"
            placeholder="🛩 visited"
            onChange={this.handleChange}
            checked={this.state.visited}
          // value={this.state.visited}
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
  color: black;
  text-align: center;
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

export default CountryForm
