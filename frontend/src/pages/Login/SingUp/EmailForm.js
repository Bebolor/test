import React, { useState } from 'react';
import styled from 'styled-components';
import { Link, useHistory  } from 'react-router-dom';
import { connect } from 'react-redux';
import Axios from '../../../axios';
import { decodeMessage } from '../../../lib/helpers';
import { PageContentPicture} from '../LeftContainer';
import OctoWall from '../RigthContainer';
import { FormContainer, LeftContainer, LeftTopBar, LinkAn, LeftMiddleBar, TitleStyled, StyledForm, InputWrapper, LoginInput, LeftBottomBar, BaseButton} from '../LeftContainer';
import { apiUserSignUp } from '../../../store/actions/userAction';
import { useDispatch } from 'react-redux';



export const OvalContainer = styled.div`
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 4%;
    
`

export const OvalBlue = styled.div`
    background: #19c5db;
    height: 10px;
    width: 10px;
    border-radius: 30px;
    margin-right: 1%;
    margin-left: 1.5%;
`

export const OvalWhite= styled.div`
    border: solid white;
    height: 6px;
    width: 6px;
    border-radius: 30px;
    margin-right: 1%;
    margin-left: 1.5%;
`
const FormContainer2 = styled(FormContainer)`
    height: 47.4%;
    
`
 const LeftTopBar2 = styled(LeftTopBar)`
    margin-bottom: 15%;
`

const LeftBottomBar2 = styled(LeftBottomBar)`
    padding: 0;
    justify-content: center;

` 


const EmailSignUp = (props) => {

    const [email, setEmail] = useState('');
    const { push } = useHistory();
    const dispatch = useDispatch();


   /*  const Continuing = (event) => {
        e.preventDefault();
        registerButtonHandler(event)
    } */


    const registerButtonHandler = (event) => {
        event.preventDefault();
        // registerUser({ email: email });
        dispatch(apiUserSignUp(email));
        // maybe check server response first
        push('/confirmation');

    };

    // register
    const registerUser = (data) => {
    const url = `reg/`;

    Axios.post(url, data)
        .then((response) => {
            console.log('User creation successful');
            push('/confirmation');
        })
        .catch((error) => {
            console.log('Creation error', error.response.data);
            decodeMessage(error.response.data);
        });
    };

    
    return (
        <PageContentPicture>

            <LeftContainer>
                
                <LeftTopBar2>
                    
                </LeftTopBar2>
                
                <FormContainer2 onSubmit={registerButtonHandler}> 
                    <LeftMiddleBar>
                        <TitleStyled>Sign Up</TitleStyled>
                    <StyledForm>
                        <InputWrapper>
                            
                            <LoginInput onChange={(event) => setEmail(event.target.value)} type='email' placeholder='Email'/>
                        </InputWrapper>
                        <LinkAn>Already have an account? <Link to='/login' >Sign In</Link></LinkAn>
                    </StyledForm>
            
                    </LeftMiddleBar>
                    <LeftBottomBar2>
                        <BaseButton type='submit'>CONTINUE</BaseButton>
                    </LeftBottomBar2>
                    
                </FormContainer2>

                <OvalContainer>
                    <OvalBlue />
                    <OvalWhite />
                    <OvalWhite />
                </OvalContainer>

            </LeftContainer>

            <OctoWall/>

        </PageContentPicture>

    )
    
}

export default connect()(EmailSignUp)