describe('Find User API Test', () => {
    it('Should find the created user', () => {
      cy.request('GET', 'https://petstore.swagger.io/v2/user/danielmorademo')
        .then((response) => {
          //console.log("response", response);
          expect(response.status).to.eq(200);
          expect(response.body.username).to.eq('danielmorademo');
          expect(response.body.firstName).to.eq('Daniel');
        });
    });
  });