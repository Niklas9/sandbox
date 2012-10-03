
/**
 * @author      Niklas Andersson <nikland@student.chalmers.se>
 * @version     0.001b
 * @since       2012-10-03
 *
 * Documentation:
 * 1. Input is read from the start in the main method, which uses getMatrix and
 *    buildMatrix methods to build up the relationship matrix c which contains
 *    the costs, where rows represent employees and columns positions.
 * 2. Class FlowNetwork builds the network flow from the given matrix c and
 *    builds up the whole structure with source, sink, vertices  etc.
 */

import java.util.*;

public class OptimalEmployment
{


    /**
     * Get Matrix values from user input
     *
     * @param  s, Java I/O scanner object
     * @param  n, integer representing number of columns
     * @return one-dimensional integer vector representing all matrix values
     */
    private static int[] getMatrix(Scanner s, int n)
    {
        int[] v = new int[n*n];
        for(int i = 0; s.hasNext(); i++)
        {
            v[i] = s.nextInt();
            if(i >= (n*n-1)) // quit if we have reached max
            {
                break;
            }
        }
        return v;
    }


    /**
     * Builds a two-dimensional integer array (a math representation of a 
     * matrix in Java) from a one-dimensional vector
     *
     * @param  m, integer representing number of rows
     * @param  n, integer representing number of columns
     * @param  v, one-dimensional integer vector with all matrix values
     * @return two-dimensional integer vector, representing the matrix
     */
    private static int[][] buildMatrix(int m, int n, int[] v)
    {
        int[][] M = new int[m][n];
        int k = 0;
        for(int i = 0; i < m; i++)
        {
            for(int j = 0; j < n; j++)
            {
                M[i][j] = v[k];
                k++;
            }
        }
        return M;
    }


    /**
     * Main method
     */
    public static void main(String[] args)
    {
        // 1. Get input
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();    // number of people/jobs
        int v[] = getMatrix(s, n);  // values from input
        int[][] c = buildMatrix(n, n, v);  // matrix containing costs

        // 2. Build network flow
        FlowNetwork G = new FlowNetwork(n, c);

        // 3. Solve problem

    }

}

class FlowNetwork
{

    private ArrayList<Vertex> persons;
    private ArrayList<Vertex> jobs;
    private Vertex s;
    private Vertex t;

    public FlowNetwork(int n, int[][] c)
    {
        // create source and sink
        this.s = new Vertex();
        this.t = new Vertex();

        // init persons and jobs
        this.persons = new ArrayList<Vertex>();
        this.jobs = new ArrayList<Vertex>();

        // build flow from employment cost matrix
        this.buildFlow(n, c);
    }

    private void buildFlow(int n, int[][] c)
    {
        // create persons and jobs
        for(int i = 0; i < n; i++)
        {
            // create vertex for each person (row)
            this.persons.add(new Vertex());
            // create vertex for each job (column)
            this.jobs.add(new Vertex());
        }

        // create employment cost edges
        for(int i = 0; i < n; i++)
        {
            Vertex p = this.persons.get(i);
            // add edge from source to person
            this.s.addEdge(p, 1);
            // add person -> job edges where applicable
            for(int j = 0; j < n; j++)
            {
                int cost = c[i][j];
                // add edge, make sure we keep cost constraints
                if(cost >= 0 && cost <= 100)
                {
                    p.addEdge(this.jobs.get(j), cost);
                    //System.out.println("Creating edge from person "+ i +" to job "+ j +" with cost "+ cost);
                }
            }
        }
    }

    public void minimize()
    {
        
    }

}

class Edge
{

    public Vertex v;
    public int cost;


    public Edge(Vertex v, int capacity)
    {
        this.v = v;
        this.cost = cost;
    }

}

class Vertex
{

    private ArrayList<Edge> edges;

    public Vertex()
    {
        this.edges = new ArrayList<Edge>();
    }
    
    public void addEdge(Vertex v, int c)
    {
        this.edges.add(new Edge(v, c));
    }

    public ArrayList<Edge> getEdges()
    {
        return this.edges;
    }

}