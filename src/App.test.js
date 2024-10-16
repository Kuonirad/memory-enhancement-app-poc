import { render, screen } from "@testing-library/react";
import App from "./App";

test("renders Memory Enhancement App header", () => {
  render(<App />);
  const headerElement = screen.getByRole("heading", {
    name: /Memory Enhancement App/i,
  });
  expect(headerElement).toBeInTheDocument();
});

test("renders main sections", () => {
  render(<App />);
  const inputSection = screen.getByRole("heading", { name: /Input Memory/i });
  const displaySection = screen.getByRole("heading", {
    name: /Memory Display/i,
  });
  const enhancementSection = screen.getByRole("heading", {
    name: /Enhancement Tools/i,
  });
  expect(inputSection).toBeInTheDocument();
  expect(displaySection).toBeInTheDocument();
  expect(enhancementSection).toBeInTheDocument();
});

test("renders footer", () => {
  render(<App />);
  const footerElement = screen.getByText(/All rights reserved/i);
  expect(footerElement).toBeInTheDocument();
});
