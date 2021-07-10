import styled from 'styled-components';

export const PageContainer = styled.div`
    width: 100%;
    min-height: 100vh;
    display: grid;
    grid-template-rows: 1fr auto;
    padding: 5vw;
`;

export const PageContent = styled.div`
    min-height: 100%;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
`;
