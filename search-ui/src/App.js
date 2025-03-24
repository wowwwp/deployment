import React from "react";

import ElasticsearchAPIConnector from "@elastic/search-ui-elasticsearch-connector";

import {
  ErrorBoundary,
  SearchProvider,
  SearchBox,
  Results,
  PagingInfo,
  ResultsPerPage,
  Paging,
  WithSearch
} from "@elastic/react-search-ui";
import { Layout } from "@elastic/react-search-ui-views";
import "@elastic/react-search-ui-views/lib/styles/styles.css";


const connector = new ElasticsearchAPIConnector(
  {
    host: "http://54.79.54.184:9200/",
    index: "cv-transcriptions",
  },
  // modify the request body to include a multi_match query as duration is a double 
  (requestBody, requestState, queryConfig) => {

    if (!requestState.searchTerm) return requestBody;
    // define the fields to search as required
    const searchFields = [
      "generated_text",
      "age",
      "gender",
      "accent",
      "duration"
    ];
    // lenient is set to true to match the query as duration expects a double
    requestBody.query = {
      multi_match: {
        query: requestState.searchTerm,
        fields: searchFields,
        lenient: true
      }
    };

    return requestBody;
  }
)


const config = {
  searchQuery: {
    result_fields: {
      generated_text: {
        snippet: {
          size: 100,
          fallback: true
        },
      },
      duration: {
        raw: {}
      },
      age: {
        raw: {}
      },
      accent: {
        raw: {}
      },
      gender: {
        raw: {}
      }
    },
    facets: {
      generated_text: {},
      duration: {},
      age: {},
      gender: {},
      accent: {}
    }
  },
  apiConnector: connector,
  alwaysSearchOnInitialLoad: true
};

export default function App() {
  return (
    <SearchProvider config={config}>
      <WithSearch mapContextToProps={({ wasSearched }) => ({ wasSearched })}>
        {({ wasSearched }) => {
          return (
            <div className="App">
              <ErrorBoundary>
                <Layout
                  header={<SearchBox />}
                  bodyContent={
                    <Results
                      titleField={"id"}
                    />
                  }
                  bodyHeader={
                    <React.Fragment>
                      {wasSearched && <PagingInfo />}
                      {wasSearched && <ResultsPerPage />}
                    </React.Fragment>
                  }
                  bodyFooter={<Paging />}
                />
              </ErrorBoundary>
            </div>
          );
        }}
      </WithSearch>
    </SearchProvider>
  );
}
