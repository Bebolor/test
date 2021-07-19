import TeamContainer from "../../pages/Profile/Teams"
import ProfileCard from "./ProfileCard";
import CurrentTournament from "./CurrentTournament";
import { useDispatch, useSelector } from 'react-redux';
import { apiUserGetData } from '../../store/actions/userAction'
import React, { useEffect } from 'react';


const Profile = () => {


    const dispatch = useDispatch();


    const user = useSelector((state) => state.user.userData);


    useEffect(() => {
        if(!user.id) {
            dispatch(apiUserGetData(localStorage.getItem('userToken')));
        }
    }, [user.id, dispatch])


    return (
        <>
            <ProfileCard user = {user}/>
            <TeamContainer/>
            <CurrentTournament/>
        </>
        )
    };

export default Profile