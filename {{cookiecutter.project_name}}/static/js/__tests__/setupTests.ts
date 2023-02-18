import { rest } from "msw";
import { setupServer } from "msw/node";

const server = setupServer(
  rest.get("http://localhost/api/lessons/:lessonId", (req, res, ctx) => {
    // get the lessonId from the ctx
    if (req.params.lessonId === "empty") {
      return res(ctx.json({ title: "" }));
    }
    return res(ctx.json({ title: "hello there." }));
  })
);

// mock window.staticFiles array with jest.fn()
window.staticFiles = jest.fn();

beforeAll(() => {
  server.listen();
  // mock window.gettext with jest and include in jsdom
  const gettext = (str) => str;
  global.gettext = gettext;
});

afterEach(() => {
  server.resetHandlers();
});

// Reset all stores after each test run
afterAll(() => {
  server.close();
});
