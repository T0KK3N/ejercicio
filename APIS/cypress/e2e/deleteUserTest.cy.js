describe('Delete User API Test', () => {
    it('Should delete the user', () => {
      cy.request('DELETE', 'https://petstore.swagger.io/v2/user/danielmorademo')
        .then((response) => {
          //console.log("response", response);
          expect(response.status).to.eq(200);
        });
    });
  });