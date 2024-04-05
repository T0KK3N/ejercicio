describe('Search Updated User API Test', () => {
    it('Should find the updated user', () => {
      cy.request('GET', 'https://petstore.swagger.io/v2/user/danielmorademo')
        .then((response) => {
          //console.log("response", response);
          expect(response.status).to.eq(200);
          expect(response.body.firstName).to.eq('demodemodemo');
          expect(response.body.email).to.eq('demodemodemo@example.com');
        });
    });
  });