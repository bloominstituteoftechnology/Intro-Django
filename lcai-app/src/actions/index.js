import axios from 'axios';

export const FETCHING_ITEMS = 'FETCHING_ITEMS';
export const FETCHED_ITEMS = 'FETCHED_ITEM';
export const ADDING_ITEM = 'ADDING_ITEM';
export const ADDED_ITEM = 'ADDED_ITEM';
export const UPDATING_ITEM = 'UPDATING_ITEM';
export const UPDATED_ITEM = 'UPDATED_ITEM';
export const DELETING_ITEM = 'DELETING_ITEM';
export const DELETED_ITEM = 'DELETED_ITEM';
export const ERROR = 'ERROR';
export const CREATING_USER = 'CREATING_USER';
export const CREATED_USER = 'CREATED_USER';
export const CREATE_USER_ERROR = 'CREATE_USER_ERROR';
export const LOG_IN_USER = 'LOG_IN_USER';
export const LOGGED_IN_USER = 'LOGGED_IN_USER';
export const LOG_IN_USER_ERROR = 'LOG_IN_USER_ERROR';
export const AUTH_USER = 'AUTH_USER';
export const LOG_OUT_USER = 'LOG_OUT_USER';

const URL = process.env.REACT_APP_API_NOTES;
const URL_REGISTER = process.env.REACT_APP_API_REGISTER;
const URL_LOGIN = process.env.REACT_APP_API_LOGIN;
const errorAction = error => {
  return {
    type: ERROR,
    message: error.message,
  };
};

export const fetchingItems = () => {
  const fetch = axios.get(URL);
  return dispatch => {
    dispatch({
      type: FETCHING_ITEMS,
    });
    fetch
      .then(response => {
        console.log('response.data', response.data);
        dispatch({
          type: FETCHED_ITEMS,
          data: response.data['Document(s) in database'],
        });
      })
      .catch(e => {
        console.log('error', e);
        dispatch(errorAction(e));
      });
  };
};
export const addingItem = newItem => {
  // console.log(newItem);
  const addItem = axios.post(URL, newItem);
  return dispatch => {
    dispatch({
      type: ADDING_ITEM,
      newItem: newItem,
    });
    addItem
      .then(response => {
        console.log('POST response.data', response.data);
        console.log(response.data['Document(s) created']);
        // console.log("newItem", newItem);
        dispatch({
          type: ADDED_ITEM,
          allItems: response.data,
          newItem: response.data['Document(s) created'],
        });
      })
      .catch(e => {
        console.log('error', e);
        dispatch(errorAction(e));
      });
  };
};
export const updatingItem = (index, id, content) => {
  console.log('PUT', { index, id, content });
  const updateItem = axios.put(`${URL}/${id}`, content);
  return dispatch => {
    dispatch({
      type: UPDATING_ITEM,
      toUpdate: id,
      content,
    });
    updateItem
      .then(response => {
        // console.log("response.data", response.data);
        dispatch({
          type: UPDATED_ITEM,
          index,
          content: { ...content, id }, // Previous code missed the id in the 'content' note -> this make imposible to update one more time the same note. In teh server side there were no problem but in Redux, because of how it is implemented the state update, the note get updates with out id.
          allItems: response.data, //
        });
      })
      .catch(e => {
        console.log('error', e);
        dispatch(errorAction(e));
      });
  };
};
export const deletingItem = (index, id) => {
  const deleteItem = axios.delete(`${URL}/${id}`);
  return dispatch => {
    dispatch({
      type: DELETING_ITEM,
      index,
      id,
    });
    deleteItem
      .then(response => {
        console.log('DELETE response.data', response.data);
        dispatch({
          type: DELETED_ITEM,
          allItems: response.data,
          index,
          id,
        });
      })
      .catch(e => {
        console.log('error', e);
        dispatch(errorAction(e));
      });
  };
};
export const ifLoggedInAuthUser = () => {
  return distpatch => {
    distpatch({
      type: AUTH_USER,
    });
  };
};
export const registerUser = newUser => {
  const createUser = axios.post(URL_REGISTER, newUser);
  return dispatch => {
    dispatch({
      type: CREATING_USER,
    });
    createUser
      .then(response => {
        const { name, username, jwt } = response.data;
        if (!jwt) {
          throw new Error('Ups, seems that you are registered but no logged in.');
          return;
        }
        localStorage.setItem('chachi', jwt);
        dispatch({
          type: CREATED_USER,
          user: { name, username },
        });
        dispatch({
          type: AUTH_USER,
        });
      })
      .catch(e => {
        console.log('error', e);
        e.type = registerUser;
        dispatch({
          type: CREATE_USER_ERROR,
          message: 'e.message',
          eType: e.type,
        });
      });
  };
};
export const logInUser = credentials => {
  console.log({ credentials });
  const logInUser = axios.post(URL_LOGIN, credentials);
  return dispatch => {
    dispatch({
      type: LOG_IN_USER,
    });
    logInUser
      .then(response => {
        console.log('response', response);
        const { name, username, jwt } = response.data;
        if (!jwt) {
          throw new Error('Ups, seems that you are registered but no logged in.');
          return;
        }
        localStorage.setItem('chachi', jwt);
        dispatch({
          type: LOGGED_IN_USER,
          user: { name, username },
        });
        dispatch({
          type: AUTH_USER,
        });
      })
      .catch(e => {
        console.log('error', e);
        e.type = registerUser;
        dispatch({
          type: LOG_IN_USER_ERROR,
          message: 'e.message',
          eType: e.type,
        });
      });
  };
};
export const logOutUser = () => {
  localStorage.removeItem('chachi');
  return dispatch => {
    dispatch({
      type: LOG_OUT_USER,
    });
  };
};
