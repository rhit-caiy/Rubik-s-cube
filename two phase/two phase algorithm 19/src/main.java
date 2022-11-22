import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Random;
import java.util.Stack;

public class main {
//	int[] cc= {0,1,2,3,4,5,6,7};
//	int[] cco= {0,0,0,0,3,3,3,3};
//	int[] ce= {0,1,2,3,4,5,6,7,8,9,10,11};
//	int[] ceo= {0,0,0,0,1,1,4,4,3,3,3,3};
	static int[][][] facetimecorner={{{2,3,1,0},{3,1,0,2},{1,0,2,3}},{{6,4,2,0},{4,2,0,6},{2,0,6,4}},{{4,5,3,2},{5,3,2,4},{3,2,4,5}},{{6,7,5,4},{7,5,4,6},{5,4,6,7}},{{5,7,1,3},{7,1,3,5},{1,3,5,7}},{{7,6,0,1},{6,0,1,7},{0,1,7,6}}};
	static int[][][] facetimeedge={{{1,2,3,0},{2,3,0,1},{3,0,1,2}},{{4,9,5,1},{9,5,1,4},{5,1,4,9}},{{5,10,6,2},{10,6,2,5},{6,2,5,10}},{{9,8,11,10},{8,11,10,9},{11,10,9,8}},{{6,11,7,3},{11,7,3,6},{7,3,6,11}},{{7,8,4,0},{8,4,0,7},{4,0,7,8}}};
	static int[][] facecorner={{0,2,3,1},{0,6,4,2},{2,4,5,3},{4,6,7,5},{3,5,7,1},{1,7,6,0}};
	static int[][] faceedge={{0,1,2,3},{1,4,9,5},{2,5,10,6},{10,9,8,11},{3,6,11,7},{0,7,8,4}};
	static int[][][] facetimedirection={{{0,5,1,3,2,4},{0,4,5,3,1,2},{0,2,4,3,5,1}},{{2,1,3,5,4,0},{3,1,5,0,4,2},{5,1,0,2,4,3}},{{4,0,2,1,3,5},{3,4,2,0,1,5},{1,3,2,4,0,5}},{{0,2,4,3,5,1},{0,4,5,3,1,2},{0,5,1,3,2,4}},{{5,1,0,2,4,3},{3,1,5,0,4,2},{2,1,3,5,4,0}},{{1,3,2,4,0,5},{3,4,2,0,1,5},{4,0,2,1,3,5}}};
	static int[][] cornerdirection={{0,5,1},{0,4,5},{0,1,2},{0,2,4},{3,2,1},{3,4,2},{3,1,5},{3,5,4}};
	static int[][] edgedirection={{0,5},{0,1},{0,2},{0,4},{1,5},{1,2},{4,2},{4,5},{3,5},{3,1},{3,2},{3,4}};
	static BigInteger[] eighteen= {new BigInteger(String.valueOf("1")),new BigInteger(String.valueOf("18")),new BigInteger(String.valueOf("324")),new BigInteger(String.valueOf("5832")),new BigInteger(String.valueOf("104976")),new BigInteger(String.valueOf("1889568")),new BigInteger(String.valueOf("34012224")),new BigInteger(String.valueOf("612220032")),new BigInteger(String.valueOf("11019960576")),new BigInteger(String.valueOf("198359290368")),new BigInteger(String.valueOf("3570467226624")),new BigInteger(String.valueOf("64268410079232")),new BigInteger(String.valueOf("1156831381426176")),new BigInteger(String.valueOf("20822964865671168")),new BigInteger(String.valueOf("374813367582081024")),new BigInteger(String.valueOf("6746640616477458432")),new BigInteger(String.valueOf("121439531096594251776")),new BigInteger(String.valueOf("2185911559738696531968")),new BigInteger(String.valueOf("39346408075296537575424")),new BigInteger(String.valueOf("708235345355337676357632")),new BigInteger(String.valueOf("12748236216396078174437376")),new BigInteger(String.valueOf("229468251895129407139872768")),new BigInteger(String.valueOf("4130428534112329328517709824")),new BigInteger(String.valueOf("74347713614021927913318776832")),new BigInteger(String.valueOf("1338258845052394702439737982976")),new BigInteger(String.valueOf("24088659210943104643915283693568")),new BigInteger(String.valueOf("433595865796975883590475106484224")),new BigInteger(String.valueOf("7804725584345565904628551916716032"))};
	
	static ArrayList<ArrayList<HashMap<BigInteger,BigInteger>>> cr= new ArrayList<>();
	static ArrayList<ArrayList<HashMap<BigInteger,BigInteger>>> cor= new ArrayList<>();
	static ArrayList<ArrayList<HashMap<BigInteger,BigInteger>>> ep4r= new ArrayList<>();
	static ArrayList<ArrayList<HashMap<BigInteger,BigInteger>>> eor= new ArrayList<>();
	
	static ArrayList<HashMap<BigInteger,BigInteger>> cr0;
	static ArrayList<HashMap<BigInteger,BigInteger>> cor0;
	static ArrayList<HashMap<BigInteger,BigInteger>> eor0;
	static ArrayList<HashMap<BigInteger,BigInteger>> ep4r0;
	static ArrayList<HashMap<BigInteger,BigInteger>> cr1;
	static ArrayList<HashMap<BigInteger,BigInteger>> ep4r1;
	//cr0,cor0,eor0,ep4r0,cr1,ep4r1
	
	static BigInteger ccn=new BigInteger("0");
	static BigInteger ccon=new BigInteger("0");
	static BigInteger cen1=new BigInteger("0");
	static BigInteger cen2=new BigInteger("10200");
	static BigInteger cen3=new BigInteger("11856");
	static BigInteger ceon=new BigInteger("0");
	
	static int dict1step=7;
	static int dict2step=8;
	static int phase1maxstep=4;
	static int cubenumber=1;
	
	public static void main(String[] args) {
		Date date=new Date();
		System.out.printf("%tF %tT\n",date,date);
		long tstart=System.currentTimeMillis();
		
		HashMap<String,Integer> cdict=new HashMap<String,Integer>();
		HashMap<String,Integer> codict=new HashMap<String,Integer>();
		HashMap<String,Integer> ep4dict=new HashMap<String,Integer>();
		HashMap<String,Integer> eodict=new HashMap<String,Integer>();
		Integer n1=0;
		
		//cdict
		for(int i=0;i<8;i++) {
			for(int j=0;j<8;j++) {
				if(i==j) {
					continue;
				}
				for(int k=0;k<8;k++) {
					if(i==k||j==k) {
						continue;
					}
					for(int l=0;l<8;l++) {
						if(i==l||j==l||k==l) {
							continue;
						}
						for(int m=0;m<8;m++) {
							if(i==m||j==m||k==m||l==m) {
								continue;
							}
							for(int n=0;n<8;n++) {
								if(i==n||j==n||k==n||l==n||m==n) {
									continue;
								}
								for(int o=0;o<8;o++) {
									if(i==o||j==o||k==o||l==o||m==o||n==o) {
										continue;
									}
									for(int p=0;p<8;p++) {
										if(i==p||j==p||k==p||l==p||m==p||n==p||o==p) {
											continue;
										}
//										Integer[] list= new Integer[]{i,j,k,l,m,n,o,p};
//										String key=Arrays.toString(list);
										String key=Integer.toString(i)+","+Integer.toString(j)+","+Integer.toString(k)+","+Integer.toString(l)+","+Integer.toString(m)+","+Integer.toString(n)+","+Integer.toString(o)+","+Integer.toString(p);
										cdict.put(key, n1);
										n1++;
									}
								}
							}
						}
					}
				}
			}
		}
		System.out.println(cdict.size());
		
		//codict
		n1=0;
		for(int i=0;i<3;i++) {
			for(int j=0;j<3;j++) {
				for(int k=0;k<3;k++) {
					for(int l=0;l<3;l++) {
						for(int m=0;m<3;m++) {
							for(int n=0;n<3;n++) {
								for(int o=0;o<3;o++) {
									for(int p=0;p<3;p++) {
										if((i+j+k+l+m+n+o+p)%3==0) {
//											Integer[] list=new Integer[] {cornerdirection[0][i],cornerdirection[1][j],cornerdirection[2][k],cornerdirection[3][l],cornerdirection[4][m],cornerdirection[5][n],cornerdirection[6][o],cornerdirection[7][p]};
//											String key=Arrays.toString(list);
											String key=Integer.toString(cornerdirection[0][i])+","+Integer.toString(cornerdirection[1][j])+","+Integer.toString(cornerdirection[2][k])+","+Integer.toString(cornerdirection[3][l])+","+Integer.toString(cornerdirection[4][m])+","+Integer.toString(cornerdirection[5][n])+","+Integer.toString(cornerdirection[6][o])+","+Integer.toString(cornerdirection[7][p]);
											codict.put(key, n1);
											n1++;
										}
									}
								}
							}
						}
					}
				}
			}
		}
		System.out.println(codict.size());
//		System.out.println(codict.get("00003333"));
		
		//ep4dict
		n1=0;
		for(int i=0;i<12;i++) {
			for(int j=i+1;j<12;j++) {
				for(int k=j+1;k<12;k++) {
					for(int l=k+1;l<12;l++) {
						String i1=Integer.toString(i);
						String j1=Integer.toString(j);
						String k1=Integer.toString(k);
						String l1=Integer.toString(l);
						ep4dict.put(i1+","+j1+","+k1+","+l1, n1+0);
						ep4dict.put(i1+","+j1+","+l1+","+k1, n1+1);
						ep4dict.put(i1+","+k1+","+j1+","+l1, n1+2);
						ep4dict.put(i1+","+k1+","+l1+","+j1, n1+3);
						ep4dict.put(i1+","+l1+","+j1+","+k1, n1+4);
						ep4dict.put(i1+","+l1+","+k1+","+j1, n1+5);
						ep4dict.put(j1+","+i1+","+k1+","+l1, n1+6);
						ep4dict.put(j1+","+i1+","+l1+","+k1, n1+7);
						ep4dict.put(j1+","+k1+","+i1+","+l1, n1+8);
						ep4dict.put(j1+","+k1+","+l1+","+i1, n1+9);
						ep4dict.put(j1+","+l1+","+i1+","+k1, n1+10);
						ep4dict.put(j1+","+l1+","+k1+","+i1, n1+11);
						ep4dict.put(k1+","+i1+","+j1+","+l1, n1+12);
						ep4dict.put(k1+","+i1+","+l1+","+j1, n1+13);
						ep4dict.put(k1+","+j1+","+i1+","+l1, n1+14);
						ep4dict.put(k1+","+j1+","+l1+","+i1, n1+15);
						ep4dict.put(k1+","+l1+","+i1+","+j1, n1+16);
						ep4dict.put(k1+","+l1+","+j1+","+i1, n1+17);
						ep4dict.put(l1+","+i1+","+j1+","+k1, n1+18);
						ep4dict.put(l1+","+i1+","+k1+","+j1, n1+19);
						ep4dict.put(l1+","+j1+","+i1+","+k1, n1+20);
						ep4dict.put(l1+","+j1+","+k1+","+i1, n1+21);
						ep4dict.put(l1+","+k1+","+i1+","+j1, n1+22);
						ep4dict.put(l1+","+k1+","+j1+","+i1, n1+23);
						n1+=24;
					}
				}
			}
		}
		System.out.println(ep4dict.size());
		
		//eodict
		n1=0;
		for(int i=0;i<2;i++) {
			for(int j=0;j<2;j++) {
				for(int k=0;k<2;k++) {
					for(int l=0;l<2;l++) {
						for(int m=0;m<2;m++) {
							for(int n=0;n<2;n++) {
								for(int o=0;o<2;o++) {
									for(int p=0;p<2;p++) {
										for(int q=0;q<2;q++) {
											for(int r=0;r<2;r++) {
												for(int s=0;s<2;s++) {
													for(int t=0;t<2;t++) {
														if((i+j+k+l+m+n+o+p+q+r+s+t)%2==0) {
															Integer[] list=new Integer[] {edgedirection[0][i],edgedirection[1][j],edgedirection[2][k],edgedirection[3][l],edgedirection[4][m],edgedirection[5][n],edgedirection[6][o],edgedirection[7][p],edgedirection[8][q],edgedirection[9][r],edgedirection[10][s],edgedirection[11][t]};
															String key=listtostring(list);
															eodict.put(key, n1);
															n1++;
														}
													}
												}
											}
										}
									}
								}
							}
						}
					}
				}
			}
		}
		System.out.println(eodict.size());
		System.out.printf("%f\n",(System.currentTimeMillis()-tstart)/(float)1000);
		
		for(int f=0;f<6;f++) {
			cr.add(new ArrayList<HashMap<BigInteger,BigInteger>>());
			cor.add(new ArrayList<HashMap<BigInteger,BigInteger>>());
			ep4r.add(new ArrayList<HashMap<BigInteger,BigInteger>>());
			eor.add(new ArrayList<HashMap<BigInteger,BigInteger>>());
			for(int t=0;t<3;t++) {
				cr.get(f).add(new HashMap<BigInteger,BigInteger>());
				cor.get(f).add(new HashMap<BigInteger,BigInteger>());
				ep4r.get(f).add(new HashMap<BigInteger,BigInteger>());
				eor.get(f).add(new HashMap<BigInteger,BigInteger>());
			}
		}
		for(int f=0;f<6;f++) {
			int c1=facecorner[f][0];
			int c2=facecorner[f][1];
			int c3=facecorner[f][2];
			int c4=facecorner[f][3];
			int e1=faceedge[f][0];
			int e2=faceedge[f][1];
			int e3=faceedge[f][2];
			int e4=faceedge[f][3];
			int[] fe=faceedge[f];
			HashSet<Integer> sfe=new HashSet<Integer>();
			sfe.add(e1);
			sfe.add(e2);
			sfe.add(e3);
			sfe.add(e4);
			for(int t=0;t<3;t++) {
				int nc1=facetimecorner[f][t][0];
				int nc2=facetimecorner[f][t][1];
				int nc3=facetimecorner[f][t][2];
				int nc4=facetimecorner[f][t][3];
				int ne1=facetimeedge[f][t][0];
				int ne2=facetimeedge[f][t][1];
				int ne3=facetimeedge[f][t][2];
				int ne4=facetimeedge[f][t][3];
				int[] fte=facetimeedge[f][t];
				int[] ftd=facetimedirection[f][t];
				
				HashMap<BigInteger,BigInteger> d=cr.get(f).get(t);
				for(String dc:cdict.keySet()) {
					Integer[] lc=stringtolist(dc);
					Integer[] c=stringtolist(dc);
					c[c1]=lc[nc1];
					c[c2]=lc[nc2];
					c[c3]=lc[nc3];
					c[c4]=lc[nc4];
					d.put(new BigInteger(String.valueOf(cdict.get(dc))),new BigInteger(String.valueOf(cdict.get(listtostring(c)))));
				}
				
				d=cor.get(f).get(t);
				for(String dco:codict.keySet()) {
					Integer[] lco=stringtolist(dco);
					Integer[] co=stringtolist(dco);
					co[c1]=ftd[lco[nc1]];
					co[c2]=ftd[lco[nc2]];
					co[c3]=ftd[lco[nc3]];
					co[c4]=ftd[lco[nc4]];
					d.put(new BigInteger(String.valueOf(codict.get(dco))),new BigInteger(String.valueOf(codict.get(listtostring(co)))));
				}
				
				d=ep4r.get(f).get(t);
				for(String dep:ep4dict.keySet()) {
					Integer[] lep=stringtolist(dep);
					Integer[] ep=stringtolist(dep);
					for(int i=0;i<4;i++) {
						if(sfe.contains(ep[i])) {
							ep[i]=fe[index(fte,lep[i])];
						}
					}
					d.put(new BigInteger(String.valueOf(ep4dict.get(dep))),new BigInteger(String.valueOf(ep4dict.get(listtostring(ep)))));
				}
				
				d=eor.get(f).get(t);
				for(String deo:eodict.keySet()) {
					Integer[] leo=stringtolist(deo);
					Integer[] eo=stringtolist(deo);
					eo[e1]=ftd[leo[ne1]];
					eo[e2]=ftd[leo[ne2]];
					eo[e3]=ftd[leo[ne3]];
					eo[e4]=ftd[leo[ne4]];
					d.put(new BigInteger(String.valueOf(eodict.get(deo))),new BigInteger(String.valueOf(eodict.get(listtostring(eo)))));
				}
				
			}
		}
		System.out.printf("initialized time %.3fs\n",(System.currentTimeMillis()-tstart)/(float)1000);
		
		cr0=new ArrayList<HashMap<BigInteger,BigInteger>>();
		for(ArrayList<HashMap<BigInteger,BigInteger>> a:cr) {
			cr0.add(a.get(0));
		}
		
		cor0=new ArrayList<HashMap<BigInteger,BigInteger>>();
		for(ArrayList<HashMap<BigInteger,BigInteger>> a:cor) {
			cor0.add(a.get(0));
		}
		
		eor0=new ArrayList<HashMap<BigInteger,BigInteger>>();
		for(ArrayList<HashMap<BigInteger,BigInteger>> a:eor) {
			eor0.add(a.get(0));
		}
		
		ep4r0=new ArrayList<HashMap<BigInteger,BigInteger>>();
		for(ArrayList<HashMap<BigInteger,BigInteger>> a:ep4r) {
			ep4r0.add(a.get(0));
		}
		
		cr1=new ArrayList<HashMap<BigInteger,BigInteger>>();
		for(ArrayList<HashMap<BigInteger,BigInteger>> a:cr) {
			cr1.add(a.get(1));
		}
		
		ep4r1=new ArrayList<HashMap<BigInteger,BigInteger>>();
		for(ArrayList<HashMap<BigInteger,BigInteger>> a:ep4r) {
			ep4r1.add(a.get(1));
		}
		System.out.printf("%d + %d\n",dict1step,dict2step);
		long tdict0=System.currentTimeMillis();
		HashMap<BigInteger,BigInteger> dict1=getdict1(dict1step);
		long tdict1=System.currentTimeMillis();
		HashMap<BigInteger,BigInteger> dict2=getdict2(dict2step);
		long tdict2=System.currentTimeMillis();
		System.out.printf("%3fs = %.3fs + %.3fs\n",(tdict2-tdict0)/(float)1000,(tdict1-tdict0)/(float)1000,(tdict2-tdict1)/(float)1000);

		int stepshouldbelow=phase1maxstep+dict1step+dict2step+1;
		for(int i=0;i<cubenumber;i++) {
			System.out.printf("\ncube %d\n", i);
			System.out.printf("%tF %tT\n",date,date);
			System.out.printf("search depth %d + %d + %d = %d\n",phase1maxstep,dict1step,dict2step,stepshouldbelow-1);
			String[] randomstrings=randomcube();
			System.out.println(randomstrings[0]);
			System.out.println(randomstrings[1]);
			Cubepack[] unsolvedcubes=new Cubepack[6];
			for(int base=0;base<3;base++) {
				unsolvedcubes[base]=getcubewithbase(randomstrings[0],base);
			}
			for(int base=0;base<3;base++) {
				unsolvedcubes[base+3]=getcubewithbase(randomstrings[1],base);
			}
			Solvereturn solvereturn=new Solvereturn(stepshouldbelow,stepshouldbelow*2,eighteen[stepshouldbelow]);
			for(int j=0;j<6;j++) {
				solvereturn=solve(unsolvedcubes[j],solvereturn);
			}
		}
	}
	
	
	private static Solvereturn solve(Cubepack cubepack, Solvereturn solvereturn) {
		long tstart=System.currentTimeMillis();
		Stack cubes=new Stack();
		cubes.add(new solvecube(cubepack.c,cubepack.co,cubepack.eo,cubepack.e1,cubepack.e2,cubepack.e3,new BigInteger("1"),0,-1));
		int htm=solvereturn.htm;
		int qtm=solvereturn.qtm;
		BigInteger minmove=solvereturn.minmove;
		return new Solvereturn(htm,qtm,minmove);
	}


	public static String[] randomcube() {
		Random r=new Random();
		int a=r.nextInt(512)+512;
		System.out.printf("random with %d moves\n",a);
		String[] s=new String[] {"",""};
		for(int i=0;i<a;i++) {
			int f=r.nextInt(5);
			int t=r.nextInt(2);
			s[0]+=String.valueOf(f)+String.valueOf(t);
			s[1]=String.valueOf(f)+String.valueOf(2-t)+s[1];
		}
		return s;
	}
	
	public static Cubepack getcubewithbase(String randomstring,int base) {
		Integer[] direction=new Integer[][] {{0,1,2,3,4,5},{1,2,0,4,5,3},{2,0,1,5,3,4}}[base];
		BigInteger c=ccn;
		BigInteger co=ccon;
		BigInteger e1=cen1;
		BigInteger e2=cen2;
		BigInteger e3=cen3;
		BigInteger eo=ceon;
		HashMap<BigInteger,BigInteger> ep4rft;
		for(int i=0;i<randomstring.length()/2;i++) {
			int f=direction[Integer.parseInt(randomstring.substring(2*i,2*i+1))];
			int t=Integer.parseInt(randomstring.substring(2*i+1,2*i+2));
			ep4rft=ep4r.get(f).get(t);
			c=cr.get(f).get(t).get(c);
			co=cor.get(f).get(t).get(co);
			eo=eor.get(f).get(t).get(eo);
			e1=ep4rft.get(e1);
			e2=ep4rft.get(e2);
			e3=ep4rft.get(e3);
		}
		return new Cubepack(c,co,eo,e1,e2,e3);
	}


	public static HashMap<BigInteger,BigInteger> getdict1(int dict1step){
		HashMap<BigInteger,BigInteger> dict1=new HashMap<BigInteger,BigInteger>();
		LinkedList<dict1cube> predictstate=new LinkedList<dict1cube>();
		LinkedList<dict1cube> newpredictstate=new LinkedList<dict1cube>();
		predictstate.add(new dict1cube(ccon,ceon,cen2,new BigInteger("1"),-1));
		BigInteger v1=new BigInteger("2048");
		BigInteger v2=new BigInteger("495");
		BigInteger v3=new BigInteger("24");
		BigInteger one=new BigInteger("1");
		long t0=System.currentTimeMillis();
		for(int step=1;step<dict1step+1;step++) {
			long t1=System.currentTimeMillis();
			for(dict1cube cube:predictstate) {
				BigInteger oco=cube.co;
				BigInteger oeo=cube.eo;
				BigInteger oe2=cube.e2;
				BigInteger oldstep=cube.oldstep;
				int f1=cube.f1;
				
				oldstep=oldstep.multiply(eighteen[1]);
				for(int f=0;f<6;f++) {
					if(f!=f1&&f1-f!=3) {
						BigInteger newstep=oldstep.add(new BigInteger(String.valueOf(3*f+2)));
						BigInteger nco=oco;
						BigInteger neo=oeo;
						BigInteger ne2=oe2;
						HashMap<BigInteger, BigInteger> corf0 = cor0.get(f);
						HashMap<BigInteger, BigInteger> eorf0 = eor0.get(f);
						HashMap<BigInteger, BigInteger> ep4rf0 = ep4r0.get(f);
						for(int t=0;t<3;t++) {
							nco=corf0.get(nco);
							neo=eorf0.get(neo);
							ne2=ep4rf0.get(ne2);
							BigInteger key1=nco.multiply(v1).add(neo).multiply(v2).add(ne2.divide(v3));
							if(!dict1.containsKey(key1)) {
								dict1.put(key1,newstep);
								if(step!=dict1step) {
									newpredictstate.add(new dict1cube(nco,neo,ne2,newstep,f));
								}
							}
							newstep.subtract(one);
						}
					}
				}
			}
			System.out.printf("1 %d %d %d %.3fs\n",step,newpredictstate.size(),dict1.size(),(System.currentTimeMillis()-t1)/(float)1000);
			predictstate=newpredictstate;
			newpredictstate=new LinkedList<dict1cube>();
		}
		System.out.printf("1 total %d %.3fs\n",dict1.size(),(System.currentTimeMillis()-t0)/(float)1000);
		return dict1;
	}
	
	public static HashMap<BigInteger,BigInteger> getdict2(int dict2step){
		HashMap<BigInteger,BigInteger> dict2=new HashMap<BigInteger,BigInteger>();
		LinkedList<dict2cube> predictstate=new LinkedList<dict2cube>();
		LinkedList<dict2cube> newpredictstate=new LinkedList<dict2cube>();
		predictstate.add(new dict2cube(ccn,cen1,cen2,cen3,new BigInteger("0"),-1));
		dict2.put(new BigInteger("121187856"), new BigInteger("1"));
		BigInteger mul=new BigInteger("11880");
		long t0=System.currentTimeMillis();
		for(int step=1;step<dict2step+1;step++) {
			long t1=System.currentTimeMillis();
			for(dict2cube cube:predictstate) {
				BigInteger oc=cube.c;
				BigInteger oe1=cube.e1;
				BigInteger oe2=cube.e2;
				BigInteger oe3=cube.e3;
				BigInteger oldstep=cube.oldstep;
				int f1=cube.f1;
				for(Integer f:new Integer[] {0,3}) {
					if(f!=f1&&(f1!=3||f!=3)) {
						BigInteger nc=oc;
						BigInteger ne1=oe1;
						BigInteger ne2=oe2;
						BigInteger ne3=oe3;
						HashMap<BigInteger, BigInteger> crf0 = cr0.get(f);
						HashMap<BigInteger, BigInteger> ep4rf0 = ep4r0.get(f);
						for(int t=2;t>-1;t--) {
							nc=crf0.get(nc);
							ne1=ep4rf0.get(ne1);
							ne2=ep4rf0.get(ne2);
							ne3=ep4rf0.get(ne3);
							BigInteger key2=nc.multiply(mul).add(ne1).multiply(mul).add(ne2).multiply(mul).add(ne3);
							if(!dict2.containsKey(key2)) {
								BigInteger newstep=oldstep.add(new BigInteger(String.valueOf(3*f+t)).multiply(eighteen[step-1]));
								if(step!=dict2step) {
									newpredictstate.add(new dict2cube(nc,ne1,ne2,ne3,newstep,f));
								}
								dict2.put(key2,newstep.add(eighteen[step]));
							}
						}
					}
				}
				for(Integer f:new Integer[] {1,2,4,5}) {
					if(f!=f1&&f1-f!=3) {
						HashMap<BigInteger, BigInteger> ep4rf1 = ep4r1.get(f);
						BigInteger nc=cr1.get(f).get(oc);
						BigInteger ne1=ep4rf1.get(oe1);
						BigInteger ne2=ep4rf1.get(oe2);
						BigInteger ne3=ep4rf1.get(oe3);
						BigInteger key2=nc.multiply(mul).add(ne1).multiply(mul).add(ne2).multiply(mul).add(ne3);
						if(!dict2.containsKey(key2)) {
							BigInteger newstep=oldstep.add(new BigInteger(String.valueOf(3*f+1)).multiply(eighteen[step-1]));
							if(step!=dict2step) {
								newpredictstate.add(new dict2cube(nc,ne1,ne2,ne3,newstep,f));
							}
							dict2.put(key2,newstep.add(eighteen[step]));
						}
					}
				}
			}
			System.out.printf("2 %d %d %d %.3fs\n",step,newpredictstate.size(),dict2.size(),(System.currentTimeMillis()-t1)/(float)1000);
			predictstate=newpredictstate;
			newpredictstate=new LinkedList<dict2cube>();
		}
		System.out.printf("2 total %d %.3fs\n",dict2.size(),(System.currentTimeMillis()-t0)/(float)1000);
		return dict2;
	}
	
	private static int index(int[] list, Integer value) {
		for(int i=0;i<list.length;i++) {
			if(list[i]==value) {
				return i;
			}
		}
		return -1;
	}
	public static String listtostring(Integer[] list) {
		String s="";
		for(Integer i:list) {
			s+=","+String.valueOf(i);
		}
		s=s.substring(1);
		return s;
	}
	public static Integer[] stringtolist(String s) {
		String[] slist=s.split(",");
		Integer[] list = new Integer[slist.length];
		for(int i=0;i<slist.length;i++) {
			list[i]=Integer.parseInt(slist[i]);
		}
		return list;
	}
}
