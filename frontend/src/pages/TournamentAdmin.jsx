import styled from 'styled-components';
import StartButton from '../components/StartButton'
import TournamentCard from "../components/TournamentCard";



const MainContainer = styled.div`
    
    width: 50%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    color: white;
`


const Invitations = styled.div`  
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-content: center;
    width: 100%; 
    height: 11em;



`
const Counter = styled.div`
    transform: skewX(-15deg);
    border-radius: 30px;
    border: solid 3px #19c5db;
    width: max-content;
    text-align:center;




    div.number {
        font-size: 10em;
        padding-left: 50px;
        padding-right: 50px;

    }

    div.invitation {
        font-size: 2em;
    }




`



const Home = () => {
    return (
                    <MainContainer>
                        <StartButton text={'INVITE'}/>
                        <Invitations>
                            <Counter>
                                <div className='number'>10 </div> 
                                <div className='invitation'>open invitations</div>
                            </Counter>
                            <Counter>
                                <div className='number'>12 </div> 
                                <div className='invitation'>participants</div>                        
                            </Counter>
                        </Invitations>
                        <TournamentCard/>
                        <StartButton text={'START'}/>
                    </MainContainer>
    )
}


export default Home