import React, { Component } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

class MusicList extends Component {
    constructor(props) {
        super(props);
        this.state = {
            music: [],
        }
    }
    componentDidMount() {
        let promise = axios.get(`http://localhost:8000/api/music/`);
        promise.then((response) => {
            console.log("CDM music", response.data);
            this.setState({
                music: response.data
            });
            })
            .catch((error) => {
                console.error(error);
            })
    }
    render() {
        console.log(this.state.music);
        return (
            <div>
                <div className="main-note-container">
                    {this.state.music.map(music => {
                        return (
                            <div key={music.id} className="note-indiv">
                                <h1 className="note-title">{music.title}</h1>   
                                <h3 className="note-composer">{music.composer_first_name}</h3>
                                <h3 className="note-composer">{music.composer_last_name}</h3>
                                <h5 className="note-publisher">{music.publisher}</h5>
                                <p className="note-notes">{music.notes}</p>
                            </div>              )
                    })}
                </div>
            </div>
        );
    }
    }
    
    export default MusicList;




